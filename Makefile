.PHONY: help validate format
.ONESHELL:

SHELL := /bin/bash

help:
	@echo "PZ Scripts Data Block Schema"
	@echo "Available targets:"
	@echo "  validate  - Validate all block definitions against the schema"
	@echo "  format    - Format all block definitions"

validate:
	./.venv/bin/python ./src/validateBlocks.py

format:
	./.venv/bin/python ./src/formatBlocks.py