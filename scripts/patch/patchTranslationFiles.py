# update to 42.15
import os, yaml

translation_files_path = os.path.join(os.path.dirname(__file__), "../../data/translation_files")

for file in os.listdir(translation_files_path):
    if file.endswith(".yaml"):
        with open(os.path.join(translation_files_path, file), "r") as f:
            data = yaml.safe_load(f)

        print(data["name"])

        if "filePrefix" in data:
            # Update the fileName field
            data["fileName"] = data["filePrefix"]
            data.pop("filePrefix", None)
            data.pop("fileStarter", None)

        if "function" not in data:
            data["function"] = "getText"

        with open(os.path.join(translation_files_path, file), "w") as f:
            yaml.dump(data, f, sort_keys=False)