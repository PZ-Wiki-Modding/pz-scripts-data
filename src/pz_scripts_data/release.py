import datetime
import argparse
import subprocess

from pz_scripts_data import Manifest, MANIFEST_FILE, BuildVersion, ReleaseVersion

def assert_release_exists(version: str, manifest: Manifest) -> None:
    ...
    

def main():
    MANIFEST_DATA = Manifest.load_manifest()

    parser = argparse.ArgumentParser(
        description=f"""Release a dataset build.
Current latest build: {MANIFEST_DATA.latest_build}
Current stable: {MANIFEST_DATA.stable}

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
""",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("--set-stable", type=str, 
                        help="Move the stable to the provided build version")
    parser.add_argument("--set-latest-build", type=str, 
                        help="Update the latest build version in the manifest")
    parser.add_argument("--set-latest-release", type=str, 
                        help="Update the latest release version in the manifest")
    parser.add_argument("--build", type=BuildVersion.from_string, 
                        help="Specify the new build version")
    parser.add_argument("--dry-run", action="store_true", 
                        help="Perform a dry run without making any changes")
    args = parser.parse_args()

    latest_build = MANIFEST_DATA.latest_build
    BuildVersion.assert_release_number(latest_build)

    # handle set-latest-build argument
    set_latest_build : str = args.set_latest_build
    set_latest_release : str = args.set_latest_release
    set_stable : str = args.set_stable
    dry_run : bool = args.dry_run

    pushed_new_release = None
    if set_latest_build is not None:
        print(f"Setting latest build to {set_latest_build}")
        splitted = set_latest_build.split('.')
        if len(splitted) != 3:
            raise ValueError("Invalid build version format. Expected format: 'major.minor.patch'")

        # set new version in the manifest
        MANIFEST_DATA.latest_build = BuildVersion.from_string(set_latest_build)

    # set new stable
    elif set_stable:
        print(f"Setting stable to {set_stable}")
        ReleaseVersion.assert_release_with_version(set_stable)
        MANIFEST_DATA.stable = set_stable

    # handle set-latest-release argument
    elif set_latest_release is not None:
        print(f"Setting latest release to {set_latest_release}")
        ReleaseVersion.assert_release_with_version(set_latest_release)

        # get associated release
        releases = MANIFEST_DATA.releases
        if set_latest_release not in releases.keys():
            raise ValueError(f"Release version {set_latest_release} not found in manifest")
        MANIFEST_DATA.latest_release = set_latest_release

    # no args, push a new release
    else:
        print("Pushing a new release")
        current_date = datetime.datetime.now().isoformat()
        releases = MANIFEST_DATA.releases
        build: BuildVersion = args.build if args.build is not None else latest_build
        version = 0
        if build not in releases.keys():
            releases[build] = Release(
                version=version, 
                date=current_date
            )
        else:
            existing_build = releases[build]
            existing_build.date = current_date
            existing_build.version += 1
            version = existing_build.version
        pushed_new_release = f"{build}.{version}"

    # write latest changes
    if not dry_run:
        MANIFEST_FILE.write_text(MANIFEST_DATA.model_dump_json(indent=4))

    # commit latest manifest changes
    input("Commit changes? Press Enter to continue...")
    try:
        if not dry_run:
            subprocess.run(["git", "add", str(MANIFEST_FILE)], check=True)
            message = "manifest"
            if pushed_new_release is not None:
                message += f": {pushed_new_release}"
            elif set_stable is not None:
                message += f": New stable {set_stable}"
            elif set_latest_release is not None:
                message += f": New latest release {set_latest_release}"
            elif set_latest_build is not None:
                message += f": New latest build {set_latest_build}"
            subprocess.run(["git", "commit", "-m", message], check=True)
        else:
            print("Dry run, not committing changes")
    except Exception as e:
        print(f"Error committing changes: {e}")

    # that one we don't ignore, since that could been connection issues
    input("Push changes? Press Enter to continue...")
    if not dry_run:
        subprocess.run(["git", "push"], check=True)
    else:
        print("Dry run, not pushing changes")

    # if set as stable is active
    # move stable tag
    if set_stable is not None:
        input("Move stable tag? Press Enter to continue...")
        if not dry_run:
            subprocess.run(["git", "tag", "-fa", "stable", "-m", "Moved stable tag"], check=True)
            subprocess.run(["git", "push", "-f", "--tags"], check=True)
            print(f"Moved stable tag")
        else:
            print("Dry run, not moving stable tag")

    if pushed_new_release is not None:
        input("Push new release? Press Enter to continue...")
        if not dry_run:
            subprocess.run(["git", "tag", "-fa", pushed_new_release, "-m", "New release"], check=True)
            subprocess.run(["git", "push", "-f", "--tags"], check=True)
            print(f"Pushed new release: {pushed_new_release}")
        else:
            print("Dry run, not pushing new release")



if __name__ == "__main__":
    main()