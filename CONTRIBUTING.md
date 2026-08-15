# Contributing
Each Scripts blocks have their own data file in the `data/blocks` folder. When it comes to [root files](https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/root_files.html), those are stored in the `data/roots` folder. Both root files and Scripts blocks share the same data syntax besides one or two differences.

Preferably, install the extension [YAML Language Support by Red Hat](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml) for VSCode to get syntax highlighting and validation of the YAML files.

For a detailed explanation of the data syntax, check the [schema](schemas/blocks.json) file.

## Structure
The repository is structured in the following way:
```bash
📁 .github                        # automation workflows
📁 .vscode                        # VSCode settings, notably to apply the YAML schemas
📁 data                           # holds the dataset
    📁 blocks                       # each YAML file is associated to one script block
    📁 roots                        # each YAML file describes a type of script file
📁 out                            # the formatted data for easy distribution
    📄 itemParameters.json          # parameters of item script blocks which required a specific ItemType value
    📄 roots.json                   # every root files definition in a single file
    📄 scriptsBlocks.json           # every scripts blocks definition in a single file
📁 schemas                        # JSON schemas that describe the data files
    📄 blocks.json                  # main definitions for the data files
📁 scripts                        # utilitary Python scripts for debugging
📁 src                            # Python files to format and validate the dataset
    📁 pz_scripts_data              # package 
        📄 blocks.py                  # enums of properties
        📄 formatBlocks.py            # outputs out/scriptsBlocks.json and out/roots.json
        📄 sortItemParameters.py      # outputs out/itemParameters.json
        📄 validateBlocks.py          # validates every YAML files against the schemas/blocks.json
📄 .gitignore
📄 CONTRIBUTING.md
📄 LICENSE
📄 Makefile                       # default commands to format and validate the dataset
📄 pyproject.toml                 # Python package definitions (dependencies)
📄 README.md
```

## Data format
The [Scripts wiki page](https://pzwiki.net/wiki/Scripts) does the job of explaining the syntax and elements of scripts so I suggest reading through that. The [blocks.json](schemas/blocks.json) file explains the structure of the data files and its different elements.
- Script blocks correspond to the different major sections of scripts, such as `item`, `vehicle`, `model`, etc.
- Parameters are written inside script blocks with the syntax `parameter = value,`. They can have the following attributes defined:
- Properties (different from the "Properties" section in the [wiki](https://pzwiki.net/wiki/Scripts#Properties)) are special parameters based on specific blocks, such as the `inputs` block which doesn't follow normal `parameter = value` syntax. They may not follow the same structure as parameters. Preferably ignore those.

Each parameters can have different properties based on their behavior, the usual are:
- `description`
- `type`
- `default`

## Pull requests
Whenever you do a pull request or a push to the branches `main` or `dev`, the JSON files in [out](out/) will be formatted via a GitHub action, which is used to allow for a single source of data for all script blocks. The smaller YAML files are easier to manage and work with during development but make fetching from GitHub the last dataset annoying.

The format of the data files will also be validated against the JSON schema automatically to ensure that the data is consistent and follows the expected structure. The [PZ API Docs](https://pz-wiki-modding.github.io/PZ-API-Docs/index.html) will be updated to reflect any changes made to the data files after they have been accepted, so ensure that the information is accurate and up-to-date with the latest version.

## Commits
Preferably, commits should have the following prefix for clarity:
- `DATA`: for changes in the data files.
- `DOC`: for changes in the documentation (README, CONTRIBUTING, and ScriptsDocs). Also includes schemas.
- `SCRIPT`: for changes in the script files (e.g., formatting scripts, data generation scripts, etc.).
- `OTHER`: for changes that don't fit in the above categories.
- `CHORE`: should not use, these are used for automated workflows to indicate commits from the GitHub bot.

## Contact
You can find the creator of this dataset (SimKDT) in the [PZ Modding Community](https://pzwiki.net/wiki/PZ_Modding_Community).

## License
See [LICENSE](LICENSE) for more information.