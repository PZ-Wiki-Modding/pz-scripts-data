Provides information regarding various script blocks and parameters of Project Zomboid [scripts](https://pzwiki.net/wiki/Scripts) system. This dataset is used to provide a [ScriptsDocs](https://sirdoggyjvla.github.io/pz-scripts-data/).

# Contributing
To contribute to the dataset, follow these steps to set up your development environment:
1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```
3. Activate the virtual environment:
   - Linux/Mac: `source .venv/bin/activate`
   - Windows: `.venv\Scripts\activate`
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Install pre-commit hooks:
   ```bash
   pre-commit install
   ```

This will format the singular JSON file on each commit, which is used to allow for a single source of truth for all script blocks. The smaller JSON files are easier to manage and work with during development.

## Script blocks
Script blocks can have the following attributes:
- `name`: The name of the block. (required)
- `description`: A brief description of what the block does. (required)
- `shouldHaveParent`: A boolean indicating whether the block should have a parent block or not.
- `parents`: A list of block names that can be parents to this block.
- `needsChildren`: A list of block names that are required as children of this block.
- `ID`: A dictionary about the ID attribute of the block. If not given, the block can't have any ID.
- `softOverride`: A boolean indicating whether the block can be [soft overridden](https://pzwiki.net/wiki/Scripts#Soft_overrides) in scripts.
- `parameters`: A list of parameters associated with the block.
- `isVariant`: Indicates if this block is a variant of another block, notably used for blocks which have different definitions based on the ID attribute, such as `component` blocks. The value is the original block name.

### ID
The `ID` dictionary can have the following attributes:
- `parentsWithout`: A list of block names that cannot be parents if this block has an ID.
- `values`: A list of allowed ID values for this block. If not given, any value is allowed.
- `asType`: Specifies if the ID of the block should count as the block type. For example components have specific definitions based on their ID. This means a script block needs to be defined with the name `component <componentID>` as well as `component` to cover all component types available from the ID with the `values` attribute.

## Parameters
Parameters are written inside script blocks with the syntax `parameter = value`. They can have the following attributes defined:
- `name`: The name of the parameter. (required)
- `#ref`: A reference to another block parameter.
- `description`: A brief description of what the parameter does. Examples should use `cpp` code blocks for scripts for clarity.
- `allowedDuplicate`: A boolean indicating whether the parameter can be duplicated.
- `canBeEmpty`: A boolean indicating whether the parameter can be empty.
- `itemTypes`: Specifies an array of the type of items the parameter is associated with (e.g., "vehicle", "item", etc.). Only for item scripts.
- `parentsOnly`: A list of parent block types for which this parameter is applicable.
- `required`: A boolean indicating whether the parameter is required.
- `default`: The default value of the parameter if not provided.
- `type`: The data type of the parameter (e.g., "string", "float", "int", etc.).
- `values`: A list of allowed values for the parameter.
- `deprecated`: A boolean indicating whether the parameter is deprecated.

## Properties
Properties are special parameters based on specific blocks, such as the `inputs` block which doesn't follow normal `parameter = value` syntax. They may not follow the same structure as parameters.