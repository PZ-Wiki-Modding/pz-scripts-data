import json
import datetime
from typing import Any, TypeVar, Generic
from pathlib import Path
from pydantic import BaseModel, GetCoreSchemaHandler, GetJsonSchemaHandler
from pydantic_core import core_schema
from pydantic.json_schema import JsonSchemaValue

WORKSPACE = Path(__file__).parent.parent.parent
MANIFEST_FILE = WORKSPACE / "manifest.json"


P = TypeVar("P", bound=tuple[int, ...])

class BaseVersion(Generic[P]):
    pattern: str
    def __init__(self, *args: int):
        self._parts: P = args  # type: ignore - due to generic tuple type not being passable to __init__ directly

    def __str__(self) -> str:
        return ".".join(map(str, self._key()))

    def _key(self) -> P:
        return self._parts

    def __repr__(self) -> str:
        return f"{type(self).__name__}({str(self)})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, BaseVersion): return NotImplemented
        return self._key() == other._key()

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, BaseVersion): return NotImplemented
        return self._key() < other._key()

    def __le__(self, other: object) -> bool:
        if not isinstance(other, BaseVersion): return NotImplemented
        return self._key() <= other._key()

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, BaseVersion): return NotImplemented
        return self._key() > other._key()

    def __ge__(self, other: object) -> bool:
        if not isinstance(other, BaseVersion): return NotImplemented
        return self._key() >= other._key()

    def __hash__(self) -> int:
        return hash((type(self), str(self)))

    @classmethod
    def from_string(cls, version: str) -> 'BaseVersion':
        raise NotImplemented

    @classmethod
    def __get_pydantic_core_schema__(cls, source: Any, handler: GetCoreSchemaHandler) -> core_schema.CoreSchema:
        return core_schema.no_info_plain_validator_function(
            lambda v: v if isinstance(v, cls) else cls.from_string(str(v)),
            serialization=core_schema.plain_serializer_function_ser_schema(str),
        )

    @classmethod
    def __get_pydantic_json_schema__(cls, schema: core_schema.CoreSchema, handler: GetJsonSchemaHandler) -> JsonSchemaValue:
        return {"type": "string", "pattern": cls.pattern}



class BuildVersion(BaseVersion[tuple[int, int, int]]):
    pattern: str = r"^\d+\.\d+\.\d+$"
    def __init__(self, major: int, minor: int, patch: int):
        super().__init__(major, minor, patch)
        self.major = major
        self.minor = minor
        self.patch = patch

    @staticmethod
    def assert_release_number(version: 'str | BuildVersion') -> tuple[int, int, int]:
        splitted = str(version).split('.')
        if len(splitted) != 3:
            raise ValueError("Invalid build version format. Expected format: 'major.minor.patch'")
        try:
            major, minor, patch = [int(x) for x in splitted]
        except ValueError:
            raise ValueError("Invalid build version format. Expected format: 'major.minor.patch' with integers")
        except Exception as e:
            raise ValueError(f"Error parsing build version: {e}")
        return major, minor, patch

    @classmethod
    def from_string(cls, version: str) -> 'BuildVersion':
        major, minor, patch = cls.assert_release_number(version)
        return cls(major, minor, patch)

    def to_release_version(self, release_version: int) -> 'ReleaseVersion':
        """Convert the current build version to a release version
        with the specified release version number."""
        return ReleaseVersion(self.major, self.minor, self.patch, release_version)

class ReleaseVersion(BaseVersion[tuple[int, int, int, int]]):
    pattern: str = r"^\d+\.\d+\.\d+\.\d+$"
    def __init__(self, major: int, minor: int, patch: int, release_version: int):
        super().__init__(major, minor, patch, release_version)
        self.major: int = major
        self.minor: int = minor
        self.patch: int = patch
        self.release_version: int = release_version

    def _key(self) -> tuple[int, int, int, int]:
        return super()._key()

    @staticmethod
    def assert_release_with_version(version: 'str | ReleaseVersion') -> tuple[int, int, int, int]:
        splitted = str(version).split('.')
        if len(splitted) != 4:
            raise ValueError("Invalid release version format. Expected format: 'major.minor.patch.version'")
        try:
            major, minor, patch, release_version = [int(x) for x in splitted]
        except ValueError:
            raise ValueError("Invalid release version format. Expected format: 'major.minor.patch.version' with integers")
        except Exception as e:
            raise ValueError(f"Error parsing release version: {e}")
        return major, minor, patch, release_version

    @classmethod
    def from_string(cls, version: str) -> 'ReleaseVersion':
        major, minor, patch, release_version = cls.assert_release_with_version(version)
        return cls(major, minor, patch, release_version)

    def to_build_version(self) -> 'BuildVersion':
        """Convert the current release version to a build version
        by discarding the release version number."""
        return BuildVersion(self.major, self.minor, self.patch)




class Release(BaseModel):
    version: int
    date: datetime.datetime

class Manifest(BaseModel):
    latest_build: BuildVersion
    stable: ReleaseVersion
    releases: dict[BuildVersion, Release]

    @classmethod
    def load_manifest(cls) -> "Manifest":
        assert MANIFEST_FILE.exists(), f"Manifest file not found at {MANIFEST_FILE}"
        return Manifest.model_validate(json.loads(MANIFEST_FILE.read_text()))

    def make_releases_list(self) -> list[str]:
        """Retrieve a sorted list of all release versions as strings."""
        releases_list: list[str] = []
        for build, release in self.releases.items():
            for v in range(release.version+1):
                releases_list.append(str(build.to_release_version(v)))
        return sorted(releases_list)

    def get_latest_release(self) -> ReleaseVersion:
        releases_list = self.make_releases_list()
        if len(releases_list) == 0:
            raise ValueError("No releases found in the manifest")
        latest_release_str = releases_list[-1]
        return ReleaseVersion.from_string(latest_release_str)

    def get_latest_build(self) -> BuildVersion:
        return self.latest_build

    def get_releases(self) -> dict[BuildVersion, Release]:
        return self.releases

    def assert_release_exists(self, release_version: 'str | ReleaseVersion') -> None:
        release_version_str = str(release_version)
        releases_list = self.make_releases_list()
        if release_version_str not in releases_list:
            raise ValueError(f"Release version {release_version_str} not found in the manifest")

    def write(self, path: Path | str) -> None:
        path = Path(path)
        path.write_text(self.model_dump_json(indent=4))

if __name__ == "__main__":
    build1 = BuildVersion.from_string("42.22.2")
    build2 = BuildVersion.from_string("42.22.2")

    assert build1 == build2, "Build versions should be equal"