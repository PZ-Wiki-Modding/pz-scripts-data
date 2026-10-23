.PHONY: help validate format
.ONESHELL:

SHELL := /bin/bash

help:
	@echo "PZ Scripts Data Block Schema"
	@echo "Available targets:"
	@echo "  validate  - Validate all block definitions against the schema"
	@echo "  format    - Format all block definitions"
	@echo "  set_stable - Move the stable tag to the latest commit"
	@echo "  release    - Create a new dataset release based on the latest version in the manifest"
	@echo "  release_package - Build and publish the Python package"

validate:
	./.venv/bin/python ./src/pz_scripts_data/validateBlocks.py

format:
	./.venv/bin/python ./src/pz_scripts_data/formatBlocks.py
	./.venv/bin/python ./src/pz_scripts_data/sortItemParameters.py

release:
	./.venv/bin/python ./src/pz_scripts_data/release.py

release_package:
	uv build
	uv publish
	VERSION=$(shell uv version --short)
	git tag -a "v$$VERSION" -m "Release version $$VERSION"
	git push --tags
