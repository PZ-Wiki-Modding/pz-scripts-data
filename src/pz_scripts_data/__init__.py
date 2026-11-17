import json
import datetime
from typing import Any
from pathlib import Path
from pydantic import BaseModel, GetCoreSchemaHandler, GetJsonSchemaHandler
from pydantic_core import core_schema
from pydantic.json_schema import JsonSchemaValue

WORKSPACE = Path(__file__).parent.parent.parent
MANIFEST_FILE = WORKSPACE / "manifest.json"




class BuildVersion:
    pattern: str = r"^\d+\.\d+\.\d+$"
    def __init__(self, major: int, minor: int, patch: int):
        self.major = major
        self.minor = minor
        self.patch = patch

    def __str__(self) -> str:
        return f"{self.major}.{self.minor}.{self.patch}"

    def __repr__(self) -> str:
        return f"{type(self).__name__}({str(self)})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, BuildVersion):
            return NotImplemented
        return type(self) is type(other) and str(self) == str(other)

    def __hash__(self) -> int:
        return hash((type(self), str(self)))


    @classmethod
    def __get_pydantic_core_schema__(cls, source: Any, handler: GetCoreSchemaHandler) -> core_schema.CoreSchema:
        return core_schema.no_info_plain_validator_function(
            lambda v: v if isinstance(v, cls) else cls.from_string(str(v)),
            serialization=core_schema.plain_serializer_function_ser_schema(str),
        )

    @classmethod
    def __get_pydantic_json_schema__(cls, schema: core_schema.CoreSchema, handler: GetJsonSchemaHandler) -> JsonSchemaValue:
        return {"type": "string", "pattern": cls.pattern}


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
    def from_string(cls, version: str) -> "BuildVersion":
        major, minor, patch = cls.assert_release_number(version)
        return cls(major, minor, patch)

class ReleaseVersion(BuildVersion):
    pattern: str = r"^\d+\.\d+\.\d+\.\d+$"
    def __init__(self, major: int, minor: int, patch: int, release_version: int):
        super().__init__(major, minor, patch)
        self.release_version = release_version

    def __str__(self) -> str:
        return f"{self.major}.{self.minor}.{self.patch}.{self.release_version}"

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
    def from_string(cls, version: str) -> "ReleaseVersion":
        major, minor, patch, release_version = cls.assert_release_with_version(version)
        return cls(major, minor, patch, release_version)





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

if __name__ == "__main__":
    build1 = BuildVersion.from_string("42.22.2")
    build2 = BuildVersion.from_string("42.22.2")

    assert build1 == build2, "Build versions should be equal"