import re
from pathlib import Path


scripts_dir = Path("/home/simon/.steam/debian-installation/steamapps/common/ProjectZomboid/projectzomboid/media/scripts")

uniques = set()
for file in scripts_dir.rglob("*.txt"):
    with open(file, "r") as f:
        content = f.read()
        matches = re.findall(r"AttachmentType\s*=\s*(\S+),", content)
        if matches:
            uniques.update(matches)

for unique in sorted(uniques):
    print(unique)