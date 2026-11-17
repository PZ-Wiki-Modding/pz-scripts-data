import pytest
from pydantic import BaseModel, ValidationError

from pz_scripts_data import BuildVersion, ReleaseVersion


class VersionedModel(BaseModel):
    build: BuildVersion
    stable: ReleaseVersion


@pytest.mark.parametrize(
    ("text", "expected"),
    [("42.22.2", (42, 22, 2)), ("0.0.0", (0, 0, 0)), ("42.100.7", (42, 100, 7))],
)
def test_build_version_from_string_parses_parts(text: str, expected: tuple[int, int, int]):
    version = BuildVersion.from_string(text)
    assert (version.major, version.minor, version.patch) == expected
    assert str(version) == text


@pytest.mark.parametrize("text", ["42.22", "42.22.2.1", "42.22.a", "", "v42.22.2", "42..2"])
def test_build_version_from_string_rejects_invalid_input(text: str):
    with pytest.raises(ValueError, match="Invalid build version format"):
        BuildVersion.from_string(text)


def test_build_version_repr():
    assert repr(BuildVersion(42, 22, 2)) == "BuildVersion(42.22.2)"


def test_build_version_equality_and_hash():
    a = BuildVersion(42, 22, 2)
    b = BuildVersion.from_string("42.22.2")
    assert a == b
    assert hash(a) == hash(b)
    assert len({a, b}) == 1


def test_build_version_compares_numerically_not_lexically():
    versions = [BuildVersion.from_string(s) for s in ["42.10.0", "42.9.0", "41.99.99", "42.9.10"]]
    assert [str(v) for v in sorted(versions)] == ["41.99.99", "42.9.0", "42.9.10", "42.10.0"]


@pytest.mark.parametrize(("lower", "higher"), [("42.22.1", "42.22.2"), ("42.21.9", "42.22.0"), ("41.99.99", "42.0.0")])
def test_build_version_ordering_operators(lower: str, higher: str):
    lo = BuildVersion.from_string(lower)
    hi = BuildVersion.from_string(higher)
    assert lo < hi and lo <= hi and hi > lo and hi >= lo
    assert not (hi < lo) and not (hi <= lo) and not (lo > hi) and not (lo >= hi)


def test_build_version_equal_is_ordered_inclusively():
    v = BuildVersion(42, 22, 2)
    assert v <= v and v >= v
    assert not v < v and not v > v


def test_build_version_is_not_equal_to_other_types():
    assert BuildVersion(42, 22, 2) != "42.22.2"


def test_build_version_ordering_with_other_types_raises():
    with pytest.raises(TypeError):
        BuildVersion(42, 22, 2) < "42.22.3"  # type: ignore[operator]


def test_build_version_to_release_version():
    release = BuildVersion.from_string("42.22.2").to_release_version(1)
    assert isinstance(release, ReleaseVersion)
    assert release == ReleaseVersion(42, 22, 2, 1)
    assert str(release) == "42.22.2.1"


@pytest.mark.parametrize(
    ("text", "expected"),
    [("42.22.2.1", (42, 22, 2, 1)), ("0.0.0.0", (0, 0, 0, 0)), ("42.22.2.10", (42, 22, 2, 10))],
)
def test_release_version_from_string_parses_parts(text: str, expected: tuple[int, int, int, int]):
    version = ReleaseVersion.from_string(text)
    assert (version.major, version.minor, version.patch, version.release_version) == expected
    assert str(version) == text


@pytest.mark.parametrize("text", ["42.22.2", "42.22.2.1.5", "42.22.2.x", "", "42.22.2.1-beta"])
def test_release_version_from_string_rejects_invalid_input(text: str):
    with pytest.raises(ValueError, match="Invalid release version format"):
        ReleaseVersion.from_string(text)


def test_release_version_repr():
    assert repr(ReleaseVersion(42, 22, 2, 1)) == "ReleaseVersion(42.22.2.1)"


def test_release_version_to_build_version_discards_release_number():
    build = ReleaseVersion(42, 22, 2, 7).to_build_version()
    assert isinstance(build, BuildVersion)
    assert build == BuildVersion(42, 22, 2)


def test_release_version_equality_and_hash():
    a = ReleaseVersion.from_string("42.22.2.1")
    b = ReleaseVersion(42, 22, 2, 1)
    assert a == b
    assert hash(a) == hash(b)
    assert ReleaseVersion(42, 22, 2, 1) != ReleaseVersion(42, 22, 2, 2)


def test_release_version_is_not_equal_to_build_version_with_same_numbers():
    assert BuildVersion(42, 22, 2) != ReleaseVersion(42, 22, 2, 0)


def test_release_version_compares_release_number_numerically():
    versions = [ReleaseVersion.from_string(s) for s in ["42.22.2.10", "42.22.2.9", "42.22.3.0", "42.22.2.1"]]
    assert [str(v) for v in sorted(versions)] == ["42.22.2.1", "42.22.2.9", "42.22.2.10", "42.22.3.0"]


@pytest.mark.parametrize(
    ("lower", "higher"),
    [("42.22.2.1", "42.22.2.2"), ("42.22.2.9", "42.22.2.10"), ("42.22.2.10", "42.22.3.0"), ("42.22.9.5", "42.23.0.0")],
)
def test_release_version_ordering_operators(lower: str, higher: str):
    lo = ReleaseVersion.from_string(lower)
    hi = ReleaseVersion.from_string(higher)
    assert lo < hi and lo <= hi and hi > lo and hi >= lo
    assert not (hi < lo) and not (hi <= lo) and not (lo > hi) and not (lo >= hi)


def test_versions_validate_from_strings_and_serialize_to_strings():
    model = VersionedModel.model_validate({"build": "42.22.2", "stable": "42.22.2.1"})
    assert model.build == BuildVersion(42, 22, 2)
    assert model.stable == ReleaseVersion(42, 22, 2, 1)
    assert model.model_dump(mode="json") == {"build": "42.22.2", "stable": "42.22.2.1"}


def test_versions_validation_rejects_invalid_strings():
    with pytest.raises(ValidationError):
        VersionedModel.model_validate({"build": "42.22", "stable": "42.22.2.1"})
    with pytest.raises(ValidationError):
        VersionedModel.model_validate({"build": "42.22.2", "stable": "42.22.2"})
