# Contributing
Whenever you do a pull request or a push to the branches `main` or `dev`, the singular JSON file will be formatted via a GitHub action, which is used to allow for a single source of data for all script blocks. The smaller YAML files are easier to manage and work with during development but make fetching from GitHub the last dataset annoying.

The format of the data files will also be validated against the JSON schema to ensure that the data is consistent and follows the expected structure. The documentation will also be updated to reflect any changes made to the data files, ensuring that the information is accurate and up-to-date.

## Commits
Preferably, commits should have the following prefix for clarity:
- `DATA`: for changes in the data files.
- `DOC`: for changes in the documentation (README, CONTRIBUTING, and ScriptsDocs). Also includes schemas.
- `SCRIPT`: for changes in the script files (e.g., formatting scripts, data generation scripts, etc.).
- `OTHER`: for changes that don't fit in the above categories.

## Data format
The [Scripts wiki page](https://pzwiki.net/wiki/Scripts) does the job of explaining the syntax and elements of scripts so I suggest reading through that. The [blocks.json](schemas/blocks.json) file explains the structure of the data files and its different elements.

- Script blocks correspond to the different major sections of scripts, such as `item`, `vehicle`, `model`, etc.

- Parameters are written inside script blocks with the syntax `parameter = value,`. They can have the following attributes defined:

- Properties (different from the "Properties" section in the [wiki](https://pzwiki.net/wiki/Scripts#Properties)) are special parameters based on specific blocks, such as the `inputs` block which doesn't follow normal `parameter = value` syntax. They may not follow the same structure as parameters.

# License
For the license, see [LICENSE](LICENSE).