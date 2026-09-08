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

def assert_release_with_version(version: str) -> tuple[int, int, int, int]:
    splitted = version.split('.')
    if len(splitted) != 4:
        raise ValueError("Invalid release version format. Expected format: 'major.minor.patch.version'")
    try:
        major, minor, patch, release_version = [int(x) for x in splitted]
    except ValueError:
        raise ValueError("Invalid release version format. Expected format: 'major.minor.patch.version' with integers")
    except Exception as e:
        raise ValueError(f"Error parsing release version: {e}")
    return major, minor, patch, release_version

def main():
    parser = argparse.ArgumentParser(description="Release a dataset build")
    parser.add_argument("--set-stable", type=str, help="Move the stable to the provided build version")
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

    pushed_new_release = None
    if set_latest_build is not None:
        print(f"Setting latest build to {set_latest_build}")
        splitted = set_latest_build.split('.')
        if len(splitted) != 3:
            raise ValueError("Invalid build version format. Expected format: 'major.minor.patch'")
        assert_release_number(set_latest_build)

        # set new version in the manifest
        MANIFEST_DATA['latest_build'] = set_latest_build

    # set new stable
    elif set_stable:
        print(f"Setting stable to {set_stable}")
        MANIFEST_DATA['stable'] = set_stable

    # handle set-latest-release argument
    elif set_latest_release is not None:
        print(f"Setting latest release to {set_latest_release}")
        assert_release_with_version(set_latest_release)

        # get associated release
        releases = MANIFEST_DATA['releases']
        if set_latest_release not in releases.keys():
            raise ValueError(f"Release version {set_latest_release} not found in manifest")
        MANIFEST_DATA['latest_release'] = set_latest_release

    # no args, push a new release
    else:
        print("Pushing a new release")
        current_date = datetime.datetime.now().isoformat()
        releases = MANIFEST_DATA['releases']
        build = args.build if args.build is not None else f"{major}.{minor}.{patch}"
        version = 0
        if build not in releases.keys():
            releases[build] = {
                'date': current_date,
                'version': version,
            }
        else:
            existing_build = releases[build]
            existing_build['date'] = current_date
            existing_build['version'] += 1
            version = existing_build['version']
        pushed_new_release = f"{build}.{version}"

    # write latest changes
    MANIFEST_FILE.write_text(json.dumps(MANIFEST_DATA, indent=4))

    # commit latest manifest changes
    try:
        subprocess.run(["git", "add", str(MANIFEST_FILE)], check=True)
        message = "MANIFEST"
        if pushed_new_release is not None:
            message += f": {pushed_new_release}"
        elif set_stable is not None:
            message += f": New stable {set_stable}"
        subprocess.run(["git", "commit", "-m", message], check=True)
    except Exception as e:
        print(f"Error committing changes: {e}")

    # that one we don't ignore, since that could been connection issues
    subprocess.run(["git", "push"], check=True)

    # if set as stable is active
    # move stable tag
    if set_stable is not None:
        subprocess.run(["git", "tag", "-fa", "stable", "-m", "Moved stable tag"], check=True)
        subprocess.run(["git", "push", "-f", "--tags"], check=True)
        print(f"Moved stable tag")

    if pushed_new_release is not None:
        subprocess.run(["git", "tag", "-fa", pushed_new_release, "-m", "New release"], check=True)
        subprocess.run(["git", "push", "-f", "--tags"], check=True)
        print(f"Pushed new release: {pushed_new_release}")



if __name__ == "__main__":
    main()