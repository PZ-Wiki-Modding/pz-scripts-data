import datetime
import json

import pytest
from typed_argparse.parser import App

from pz_scripts_data import BuildVersion, Manifest, ReleaseVersion
from pz_scripts_data import release
from pz_scripts_data.release import LatestBuildArgs, NewReleaseArgs, ReleaseType, StableBumpArgs

MANIFEST_DATA = {
    "latest_build": "42.22.2",
    "stable": "42.21.0.1",
    "releases": {
        "42.21.0": {"version": 2, "date": "2026-10-24T19:40:47"},
        "42.22.2": {"version": 1, "date": "2026-11-17T01:08:46"},
    },
}


@pytest.fixture
def manifest_path(tmp_path, monkeypatch):
    path = tmp_path / "manifest.json"
    path.write_text(json.dumps(MANIFEST_DATA))
    monkeypatch.setattr(release, "MANIFEST_FILE", path)
    monkeypatch.setattr("pz_scripts_data.MANIFEST_FILE", path)
    return path


@pytest.fixture(autouse=True)
def git_calls(monkeypatch):
    calls = []
    monkeypatch.setattr(release.subprocess, "run", lambda args, **kwargs: calls.append(args))
    yield calls
    assert calls == [], "dry run must not invoke git"


@pytest.fixture(autouse=True)
def no_prompts(monkeypatch):
    def fail(prompt=""):
        raise AssertionError(f"unexpected prompt: {prompt}")

    monkeypatch.setattr("builtins.input", fail)


@pytest.fixture
def prompts(monkeypatch):
    asked: list[str] = []
    monkeypatch.setattr("builtins.input", lambda prompt="": asked.append(prompt) or "")
    return asked


@pytest.fixture
def written_manifests(monkeypatch):
    calls: list[Manifest] = []
    original = release.write_manifest

    def spy(manifest: Manifest, dry_run: bool = False):
        calls.append(manifest)
        original(manifest, dry_run=dry_run)

    monkeypatch.setattr(release, "write_manifest", spy)
    return calls


RUNNERS = [
    pytest.param(release.stable_bump_runner, StableBumpArgs(dry_run=True, yes=True, release=None), id="stable"),
    pytest.param(release.new_release_runner, NewReleaseArgs(dry_run=True, yes=True, build=None), id="release"),
    pytest.param(release.latest_build_runner,
                 LatestBuildArgs(dry_run=True, yes=True, build=BuildVersion.from_string("42.23.0")), id="build"),
]


def test_write_manifest_dry_run_leaves_file_untouched(manifest_path, capsys):
    before = manifest_path.read_text()
    manifest = Manifest.load_manifest()
    manifest.latest_build = BuildVersion.from_string("42.23.0")

    release.write_manifest(manifest, dry_run=True)

    assert manifest_path.read_text() == before
    assert "Dry run, not writing manifest" in capsys.readouterr().out


@pytest.mark.parametrize(
    ("release_type", "kwargs", "expected"),
    [
        (ReleaseType.STABLE, {"release_version": ReleaseVersion.from_string("42.21.0.1")},
         "manifest: Bump stable to 42.21.0.1"),
        (ReleaseType.NEW_RELEASE, {"pushed_new_release": "42.22.2.1"}, "manifest: 42.22.2.1"),
        (ReleaseType.LATEST_BUILD, {"new_build": BuildVersion.from_string("42.23.0")},
         "manifest: Bump latest build to 42.23.0"),
    ],
)
def test_commit_changes_dry_run_prints_commit_message(release_type, kwargs, expected, capsys):
    release.commit_changes(release_type, dry_run=True, yes=True, **kwargs)

    out = capsys.readouterr().out
    assert expected in out.splitlines()
    assert "Dry run, not committing changes" in out


def test_push_changes_dry_run_skips_push(capsys):
    release.push_changes(dry_run=True, yes=True)

    assert "Dry run, not pushing changes" in capsys.readouterr().out


@pytest.mark.parametrize(("runner", "args"), RUNNERS)
def test_dry_run_runner_never_writes_manifest(manifest_path, written_manifests, runner, args):
    before = manifest_path.read_text()

    runner(args)

    assert manifest_path.read_text() == before
    assert len(written_manifests) == 1


@pytest.mark.parametrize(
    ("runner", "args", "expected_prompts"),
    [
        (release.stable_bump_runner, StableBumpArgs(dry_run=True, yes=False, release=None),
         ["Commit changes?", "Push changes?", "Move stable tag?"]),
        (release.new_release_runner, NewReleaseArgs(dry_run=True, yes=False, build=None),
         ["Commit changes?", "Push changes?", "Push new release?"]),
        (release.latest_build_runner,
         LatestBuildArgs(dry_run=True, yes=False, build=BuildVersion.from_string("42.23.0")),
         ["Update latest build?", "Commit changes?", "Push changes?"]),
    ],
)
def test_dry_run_runner_asks_for_confirmation_unless_yes(manifest_path, prompts, runner, args, expected_prompts):
    runner(args)

    assert [p.split(" Press")[0] for p in prompts] == expected_prompts


def test_stable_dry_run_defaults_to_latest_release(manifest_path, capsys):
    release.stable_bump_runner(StableBumpArgs(dry_run=True, yes=True, release=None))

    out = capsys.readouterr().out
    assert "manifest: Bump stable to 42.22.2.1" in out.splitlines()
    assert "Dry run, not moving stable tag" in out


def test_stable_dry_run_uses_explicit_release(manifest_path, capsys):
    release.stable_bump_runner(StableBumpArgs(dry_run=True, yes=True,
                                              release=ReleaseVersion.from_string("42.21.0.1")))

    assert "manifest: Bump stable to 42.21.0.1" in capsys.readouterr().out.splitlines()


def test_stable_dry_run_rejects_unknown_release(manifest_path):
    with pytest.raises(ValueError, match="not found in the manifest"):
        release.stable_bump_runner(StableBumpArgs(dry_run=True, yes=True,
                                                  release=ReleaseVersion.from_string("42.99.0.0")))


def test_stable_dry_run_sets_stable_on_manifest(manifest_path, written_manifests):
    release.stable_bump_runner(StableBumpArgs(dry_run=True, yes=True,
                                              release=ReleaseVersion.from_string("42.22.2.0")))

    assert written_manifests[0].stable == ReleaseVersion.from_string("42.22.2.0")


def test_new_release_dry_run_defaults_to_latest_build(manifest_path, written_manifests):
    release.new_release_runner(NewReleaseArgs(dry_run=True, yes=True, build=None))

    assert written_manifests[0].releases[BuildVersion.from_string("42.22.2")].version == 2


def test_new_release_dry_run_bumps_existing_build(manifest_path, written_manifests):
    before = datetime.datetime.now()
    release.new_release_runner(NewReleaseArgs(dry_run=True, yes=True,
                                              build=BuildVersion.from_string("42.21.0")))
    after = datetime.datetime.now()

    entry = written_manifests[0].releases[BuildVersion.from_string("42.21.0")]
    assert entry.version == 3
    assert before <= entry.date <= after


def test_new_release_dry_run_adds_missing_build(manifest_path, written_manifests):
    before = datetime.datetime.now()
    release.new_release_runner(NewReleaseArgs(dry_run=True, yes=True,
                                              build=BuildVersion.from_string("42.23.0")))
    after = datetime.datetime.now()

    entry = written_manifests[0].releases[BuildVersion.from_string("42.23.0")]
    assert entry.version == 0
    assert before <= entry.date <= after


def test_latest_build_dry_run_keeps_latest_build(manifest_path, written_manifests, capsys):
    release.latest_build_runner(LatestBuildArgs(dry_run=True, yes=True,
                                                build=BuildVersion.from_string("42.23.0")))

    assert written_manifests[0].latest_build == BuildVersion.from_string("42.22.2")
    assert "Dry run, not updating latest build to: 42.23.0" in capsys.readouterr().out


def test_latest_build_dry_run_prints_latest_build_commit_message(manifest_path, capsys):
    release.latest_build_runner(LatestBuildArgs(dry_run=True, yes=True,
                                                build=BuildVersion.from_string("42.23.0")))

    assert "manifest: Bump latest build to 42.23.0" in capsys.readouterr().out.splitlines()


@pytest.mark.parametrize(
    "argv",
    [
        pytest.param(["release", "stable", "-d", "-y"], id="stable"),
        pytest.param(["release", "release", "-d", "-y"], id="release"),
        pytest.param(["release", "build", "42.23.0", "-d", "-y"], id="build"),
        pytest.param(["release", "stable", "--dry-run", "--yes"], id="long-flags"),
    ],
)
def test_cli_dry_run_subcommands_do_not_write_manifest(manifest_path, monkeypatch, capsys, argv):
    before = manifest_path.read_text()
    # typed_argparse binds sys.argv[1:] as a default at import time, so patch the argv it receives
    original_run = App.run
    monkeypatch.setattr(App, "run", lambda self, raw_args=None: original_run(self, argv[1:]))

    release.main()

    assert manifest_path.read_text() == before
    assert "Dry run" in capsys.readouterr().out
