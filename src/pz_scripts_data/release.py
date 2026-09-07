import json
import datetime
from pathlib import Path

def main():
    WORKSPACE = Path(__file__).parent.parent.parent
    MANIFEST_FILE = WORKSPACE / "manifest.json"
    assert MANIFEST_FILE.exists(), f"Manifest file not found at {MANIFEST_FILE}"

    BUILD_VERSION_FILE = WORKSPACE / "build_version"
    assert BUILD_VERSION_FILE.exists(), f"Build version file not found at {BUILD_VERSION_FILE}"

    MANIFEST_DATA = json.loads(MANIFEST_FILE.read_text())
    BUILD_VERSION = BUILD_VERSION_FILE.read_text().strip()
    major, minor, patch = [int(x) for x in BUILD_VERSION.split('.')]

    # cleanup versions list
    # - remove duplicates
    # - sort versions in descending order
    versions = MANIFEST_DATA['versions']
    versions = list(dict.fromkeys(versions))
    versions = sorted(versions, key=lambda v: [int(x) for x in v.split('.')], reverse=True)

    # retrieve current date
    date = datetime.datetime.now()
    year = date.year
    month = date.month
    day = date.day

    # if there is a previous release, determine the next release number
    last_release = versions[0] if versions else None
    release_number = 0
    if last_release is not None:
        version_elements = last_release.split('.')
        previous_major = int(version_elements[0])
        previous_minor = int(version_elements[1])
        previous_patch = int(version_elements[2])
        previous_year = int(version_elements[3])
        previous_month = int(version_elements[4])
        previous_day = int(version_elements[5])

        # if same day then we increment the release number
        if (    previous_major == major
            and previous_minor == minor
            and previous_patch == patch
            and previous_year == year 
            and previous_month == month 
            and previous_day == day
        ):
            release_number = int(version_elements[6]) + 1

    new_version = f"{major}.{minor}.{patch}.{year}.{month}.{day}.{release_number}"
    versions.insert(0, new_version)
    MANIFEST_DATA['versions'] = versions
    MANIFEST_DATA['latest'] = versions[0]
    MANIFEST_FILE.write_text(json.dumps(MANIFEST_DATA, indent=4))




if __name__ == "__main__":
    main()