import datetime
import argparse
import subprocess
import enum
import typed_argparse as tap

from pz_scripts_data import Manifest, MANIFEST_FILE, BuildVersion, ReleaseVersion, Release

class ReleaseType(enum.Enum):
    STABLE = enum.auto()
    NEW_RELEASE = enum.auto()
    LATEST_BUILD = enum.auto()


commit_message = {
    ReleaseType.STABLE: r"Bump stable to {release_version}",
    ReleaseType.NEW_RELEASE: r"{pushed_new_release}",
    ReleaseType.LATEST_BUILD: r"Bump latest build to {new_build}",
}

class BaseReleaseArgs(tap.TypedArgs):
    dry_run: bool = tap.arg('-d,--dry-run', default=False,
                            help="perform a dry run without making any changes")
    yes: bool = tap.arg('-y,--yes', default=False,
                         help="automatically confirm committing changes")

class StableBumpArgs(BaseReleaseArgs):
    release: ReleaseVersion | None = tap.arg('-b,--build', type=ReleaseVersion.from_string, default=None,
                                  help="specify the new release stable version")

class NewReleaseArgs(BaseReleaseArgs):
    build: BuildVersion | None = tap.arg('-b,--build', type=BuildVersion.from_string, default=None,
                                         help="specify the new build version")

class LatestBuildArgs(BaseReleaseArgs):
    build: BuildVersion = tap.arg(positional=True,
                                         help="specify the new latest build version")



def assert_release_exists(version: str, manifest: Manifest) -> None:
    ...

def write_manifest(manifest: Manifest, dry_run: bool = False):
    print(f"Writing manifest to {MANIFEST_FILE}")
    if not dry_run:
        manifest.write(MANIFEST_FILE)
    else:
        print("Dry run, not writing manifest")

def commit_changes(release_type: ReleaseType, dry_run: bool = False, yes: bool = False,
                   **kargs) -> None:
    # commit latest manifest changes
    if not yes:
        input("Commit changes? Press Enter to continue...")
    result = None
    try:
        assert release_type in commit_message, f"Unknown release type commit message: {release_type}-{release_type.name}"
        message = "manifest: " + commit_message[release_type].format(**kargs)
        print(message)
        if not dry_run:
            result = subprocess.run(["git", "add", str(MANIFEST_FILE)], check=True,
                                    capture_output=True)
            print(result.stdout.decode())
            print(result.stderr.decode())
            result = subprocess.run(["git", "commit", "-m", message], check=True,
                                    capture_output=True)
            print(result.stdout.decode())
            print(result.stderr.decode())
        else:
            print("Dry run, not committing changes")
    except Exception as e:
        if result is not None:
            print(result.stdout.decode())
            print(result.stderr.decode())
        print(f"Error committing changes: {e}")

def push_changes(dry_run: bool = False, yes: bool = False) -> None:
    # that one we don't ignore, since that could been connection issues
    if not yes:
        input("Push changes? Press Enter to continue...")
    if not dry_run:
        subprocess.run(["git", "push"], check=True)
    else:
        print("Dry run, not pushing changes")




def stable_bump_runner(args: StableBumpArgs):
    print("Bumping stable release")
    dry_run = args.dry_run
    yes = args.yes

    manifest = Manifest.load_manifest()

    # if no release version is specified, use the latest release from the manifest
    # else, verify the provided version exists
    release_version = args.release
    if release_version is None:
        release_version = manifest.get_latest_release()
    else:
        manifest.assert_release_exists(release_version)

    print(f"{release_version}")

    manifest.stable = release_version
    write_manifest(manifest, dry_run=dry_run)
    commit_changes(ReleaseType.STABLE, dry_run=dry_run, yes=yes,
                   release_version=release_version)
    push_changes(dry_run=dry_run, yes=yes)

    if not yes:
        input("Move stable tag? Press Enter to continue...")
    if not dry_run:
        subprocess.run(["git", "tag", "-fa", "stable", "-m", "Moved stable tag"], check=True)
        subprocess.run(["git", "push", "-f", "--tags"], check=True)
        print(f"Moved stable tag")
    else:
        print("Dry run, not moving stable tag")

def new_release_runner(args: NewReleaseArgs):
    print("Creating new release")
    dry_run = args.dry_run
    yes = args.yes
    current_date = datetime.datetime.now()

    manifest = Manifest.load_manifest()

    # default to latest build
    build_version = args.build
    if build_version is None:
        build_version = manifest.get_latest_build()

    # bump or create new release for the build version
    releases = manifest.get_releases()
    if build_version not in releases:
        releases[build_version] = Release(
            version=0,
            date=current_date
        )
    else:
        existing_build = releases[build_version]
        existing_build.date = current_date
        existing_build.version += 1
    pushed_new_release = str(releases[build_version])

    # push changes
    write_manifest(manifest, dry_run=dry_run)
    commit_changes(ReleaseType.NEW_RELEASE, dry_run=dry_run, yes=yes,
                   pushed_new_release=pushed_new_release)
    push_changes(dry_run=dry_run, yes=yes)

    # make a git tag for the newly released version
    if not yes:
        input("Push new release? Press Enter to continue...")
    if not dry_run:
        subprocess.run(["git", "tag", "-fa", pushed_new_release, "-m", "New release"], check=True)
        subprocess.run(["git", "push", "-f", "--tags"], check=True)
        print(f"Pushed new release: {pushed_new_release}")
    else:
        print("Dry run, not pushing new release")

def latest_build_runner(args: LatestBuildArgs):
    print("Updating latest build")
    dry_run = args.dry_run
    yes = args.yes
    new_build = args.build

    manifest = Manifest.load_manifest()

    if not yes:
        input("Update latest build? Press Enter to continue...")
    if not dry_run:
        manifest.latest_build = new_build
    else:
        print(f"Dry run, not updating latest build to: {new_build}")

    # push changes
    write_manifest(manifest, dry_run=dry_run)
    commit_changes(ReleaseType.LATEST_BUILD, dry_run=dry_run, yes=yes,
                   new_build=new_build)
    push_changes(dry_run=dry_run, yes=yes)



def main():
    manifest = Manifest.load_manifest()

    tap.Parser(
        tap.SubParserGroup(
            tap.SubParser(
                "stable",
                StableBumpArgs
            ),
            tap.SubParser(
                "release",
                NewReleaseArgs
            ),
            tap.SubParser(
                "build",
                LatestBuildArgs
            ),
        ),
        description=f"""Release a dataset build.
Current latest build: {manifest.latest_build}
Current stable: {manifest.stable}

Usage:

    # release a new manifest version on current build version
    uv run release

    # fix the stable version to the provided dataset version
    uv run release --set-stable <version>

    # update the latest build version in the manifest
    uv run release --set-latest-build <version>

    # update the latest release
    uv run release --set-latest-release <version>

    # perform a dry run without making any changes
    uv run release --dry-run
"""
    ).bind(
        stable_bump_runner,
        new_release_runner,
        latest_build_runner,
    ).run()


if __name__ == "__main__":
    main()