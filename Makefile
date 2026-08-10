.PHONY: help validate format
.ONESHELL:

SHELL := /bin/bash

help:
	@echo "PZ Scripts Data Block Schema"
	@echo "Available targets:"
	@echo "  validate  - Validate all block definitions against the schema"
	@echo "  format    - Format all block definitions"

validate:
	./.venv/bin/python ./src/pz_scripts_data/validateBlocks.py

format:
	./.venv/bin/python ./src/pz_scripts_data/formatBlocks.py