.PHONY: help validate format
.ONESHELL:

SHELL := /bin/bash

help:
	@echo "PZ Scripts Data Block Schema"
	@echo "Available targets:"
	@echo "  validate_data     Validate all block definitions against the schema"
	@echo "  format            Format all block definitions"
	@echo "  schema            Generate the schema for block definitions"
	@echo "  set_stable        Move the stable tag to the latest commit"
	@echo "  release           Create a new dataset release based on the latest version in the manifest"
	@echo "  release_package   Build and publish the Python package"

validate_data:
	uv run pytest src/pz_scripts_data/tests/test_data.py

format: validate_data
	uv run python ./src/pz_scripts_data/formatBlocks.py
	uv run python ./src/pz_scripts_data/sortItemParameters.py

schema:
	uv run python ./src/pz_scripts_data/schema.py

release_package:
	rm -rf dist
	rm -rf build

	uv build
	uv publish
	VERSION=$(shell uv version --short)
	git tag -a "v$$VERSION" -m "Release version $$VERSION"
	git push --tags
