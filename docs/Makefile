.PHONY: help clean html generate serve

help:
	@echo "Sphinx documentation builder"
	@echo "Available targets:"
	@echo "  generate  - Generate RST files from YAML block definitions"
	@echo "  html      - Build HTML documentation"
	@echo "  clean     - Remove generated documentation"
	@echo "  serve     - Serve documentation on http://localhost:8000"

clean:
	rm -rf build
	rm -f source/blocks/*.rst

generate:
	python ../scripts/generate_docs.py

html: generate
	sphinx-build -b html source build/html

serve: html
	cd build/html && python -m http.server 8000
