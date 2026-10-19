# PZ Scripts Data
Provides information regarding various script blocks and parameters of Project Zomboid [scripts](https://pzwiki.net/wiki/Scripts) system. This dataset is used to provide a [ScriptsDocs](https://pz-wiki-modding.github.io/PZ-API-Docs/).

The translation data is now moved to [pz-translation-data](https://github.com/SirDoggyJvla/pz-translation-data) and are now deprecated. The main data files holding the last updated translation data are kept for tools that may use them, but will be removed in the future.

## Installation

PZ Scripts Data can be installed via PyPI, Git, or in development mode as described below.

<details open>
<summary>PyPI</summary>

```bash
pip install pz-scripts-data
```
</details>

<details>
<summary>Git</summary>

```bash
pip install git+https://github.com/PZ-Wiki-Modding/pz-scripts-data.git
```
</details>

<details>
<summary>Dev</summary>

```bash
pip install -e .
```
</details>

## Schema
You can find a Pydantic model defining the data format in the [schema.py](src/pz_scripts_data/schema.py) file. A JSON schema file exported from this model is available in the [schemas/blocks.json](schemas/blocks.json) file.

## Contributing
This dataset is aimed to accept any contributions. See [CONTRIBUTING](CONTRIBUTING.md) for more information on how to contribute to this dataset.

## License
See [LICENSE](LICENSE) for more information.