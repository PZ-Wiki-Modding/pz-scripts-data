.PHONY: help validate format
.ONESHELL:

SHELL := /bin/bash

help:
	@echo "PZ Scripts Data Block Schema"
	@echo "Available targets:"
	@echo "  validate  - Validate all block definitions against the schema"
	@echo "  format    - Format all block definitions"
	@echo "  set_stable - Move the stable tag to the latest commit"
	@echo "  release    - Create a new release based on the latest version in the manifest"

validate:
	./.venv/bin/python ./src/pz_scripts_data/validateBlocks.py

format:
	./.venv/bin/python ./src/pz_scripts_data/formatBlocks.py
	./.venv/bin/python ./src/pz_scripts_data/sortItemParameters.py

set_stable:
	git tag -fa stable -m "Moved stable tag"
	git push -f --tags

release:
	./.venv/bin/python ./src/pz_scripts_data/release.py
	latest_release=$$(python3 -c "import json; print(json.load(open('./manifest.json'))['latest'])"); \
	echo "Latest release: $$latest_release"; \
	gh release create "$$latest_release" --title "$$latest_release" --notes "Automated release"