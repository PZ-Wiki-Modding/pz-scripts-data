import json
import datetime
import argparse
import subprocess
from pathlib import Path

def assert_release_number(version: str) -> tuple[int, int, int]:
    splitted = version.split('.')
    if len(splitted) != 3:
        raise ValueError("Invalid build version format. Expected format: 'major.minor.patch'")
    try:
        major, minor, patch = [int(x) for x in splitted]
    except ValueError:
        raise ValueError("Invalid build version format. Expected format: 'major.minor.patch' with integers")
    except Exception as e:
        raise ValueError(f"Error parsing build version: {e}")
    return major, minor, patch

def main():
    parser = argparse.ArgumentParser(description="Release a dataset build")
    parser.add_argument("--set-stable", type=str, help="Move the stable to the specified build version")
    parser.add_argument("--set-latest-build", type=str, help="Update the latest build version in the manifest")
    parser.add_argument("--set-latest-release", type=str, help="Update the latest release version in the manifest")
    parser.add_argument("--build", type=str, help="Specify the new build version")
    args = parser.parse_args()

    # retrieve manifest file
    WORKSPACE = Path(__file__).parent.parent.parent
    MANIFEST_FILE = WORKSPACE / "manifest.json"
    assert MANIFEST_FILE.exists(), f"Manifest file not found at {MANIFEST_FILE}"

    # retrieve the latest manifest data
    MANIFEST_DATA = json.loads(MANIFEST_FILE.read_text())
    latest_build = MANIFEST_DATA['latest_build']
    major, minor, patch = assert_release_number(latest_build)

    # handle set-latest-build argument
    set_latest_build = args.set_latest_build
    set_latest_release = args.set_latest_release
    set_stable = args.set_stable
    if set_latest_build is not None:
        splitted = set_latest_build.split('.')
        if len(splitted) != 3:
            raise ValueError("Invalid build version format. Expected format: 'major.minor.patch'")
        assert_release_number(set_latest_build)

        # set new version in the manifest
        MANIFEST_DATA['latest_build'] = set_latest_build

    # set new stable
    elif set_stable is not None:
        assert_release_number(set_stable)

        MANIFEST_DATA['stable'] = set_stable

    # handle set-latest-release argument
    elif set_latest_release is not None:
        assert_release_number(set_latest_release)

        # get associated release
        releases = MANIFEST_DATA['releases']
        if set_latest_release not in releases.keys():
            raise ValueError(f"Release version {set_latest_release} not found in manifest")
        MANIFEST_DATA['latest_release'] = set_latest_release

    # no args, push a new release
    else:
        current_date = datetime.datetime.now().isoformat()
        releases = MANIFEST_DATA['releases']
        build = args.build if args.build is not None else f"{major}.{minor}.{patch}"
        if build not in releases.keys():
            releases[build] = {
                'date': current_date,
                'version': 0,
            }
        else:
            existing_build = releases[build]
            existing_build['date'] = current_date
            existing_build['version'] += 1

    # write latest changes
    MANIFEST_FILE.write_text(json.dumps(MANIFEST_DATA, indent=4))

    # commit latest manifest changes
    subprocess.run(["git", "add", str(MANIFEST_FILE)], check=True)
    subprocess.run(["git", "commit", "-m", "MANIFEST"], check=True)
    subprocess.run(["git", "push"], check=True)

    # if set as stable is active
    # move stable tag
    if set_stable is not None:
        subprocess.run(["git", "tag", "-fa", "stable", "-m", "Moved stable tag"], check=True)
        subprocess.run(["git", "push", "-f", "--tags"], check=True)




if __name__ == "__main__":
    main()