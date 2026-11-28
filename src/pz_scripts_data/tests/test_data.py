#!/usr/bin/env python3
"""
Validate YAML block files against the blocks.json schema.

Usage:
    python validateBlocks.py                     # Validate all YAML files in data/blocks/
    python validateBlocks.py <file_path>         # Validate a specific file
    python validateBlocks.py <directory_path>    # Validate all YAML files in a directory
    python validateBlocks.py --help              # Show this help message
"""

import json, yaml, sys
from pathlib import Path
from jsonschema import Draft7Validator
from typing import Literal

from pz_scripts_data.schema import ScriptsBlock, DEFAULT_SCHEMA_OUTPUT, output_json_schema

# Default paths
DEFAULT_BLOCKS_DIR = Path("data/blocks")

def load_schema(schema_path: Path) -> dict:
    """Load the JSON schema from file."""
    # first generate the latest schema
    output_json_schema(schema_path)
    with open(schema_path, 'r') as f:
        return json.load(f)

def load_yaml_file(file_path: Path) -> dict:
    """Load a YAML file and return its contents."""
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)

def validate_file(file_path: Path, schema: dict) -> tuple[bool, list[str]]:
    """
    Validate a single YAML file against the schema.
    
    Returns:
        Tuple of (is_valid, error_messages)
    """
    errors = []
    try:
        data = load_yaml_file(file_path)
        
        # Handle empty files
        if data is None:
            return True, []
        
        # Validate against schema
        validator = Draft7Validator(schema)
        validation_errors = list(validator.iter_errors(data))
        
        if validation_errors:
            for error in validation_errors:
                path = ".".join(str(p) for p in error.absolute_path) or "root"
                errors.append(f"  {path}: {error.message}")
            return False, errors
        
        return True, []
        
    except yaml.YAMLError as e:
        return False, [f"  YAML Parse Error: {str(e)}"]
    except Exception as e:
        return False, [f"  Error: {str(e)}"]

def get_yaml_files(path: Path) -> list[Path]:
    """Get all YAML files from a path (file or directory)."""
    if path.is_file():
        if path.suffix.lower() in ['.yaml', '.yml']:
            return [path]
        return []
    elif path.is_dir():
        return sorted([f for f in path.glob("*.yaml")] + 
                     [f for f in path.glob("*.yml")])
    
    return []

def validate_target(target_path: Path = DEFAULT_BLOCKS_DIR) -> Literal[0] | Literal[1]:
    # Check if project root is correct
    if not DEFAULT_SCHEMA_OUTPUT.exists():
        print(f"Error: Schema not found at {DEFAULT_SCHEMA_OUTPUT}")
        print("Please run this script from the project root directory.")
        return 1
    
    # Load schema
    try:
        schema = load_schema(DEFAULT_SCHEMA_OUTPUT)
    except Exception as e:
        print(f"Error loading schema: {e}")
        return 1
    
    # Get files to validate
    if not target_path.exists():
        print(f"Error: Path not found: {target_path}")
        return 1
    
    yaml_files = get_yaml_files(target_path)
    
    if not yaml_files:
        print(f"No YAML files found in {target_path}")
        return 1
    
    # Validate files
    print(f"Validating {len(yaml_files)} file(s)...\n")
    
    valid_count = 0
    invalid_count = 0
    
    for file_path in yaml_files:
        is_valid, errors = validate_file(file_path, schema)
        
        if is_valid:
            print(f"✓ {file_path}")
            valid_count += 1
        else:
            print(f"✗ {file_path}")
            for error in errors:
                print(error)
            print()
            invalid_count += 1
    
    # Summary
    print("\n" + "="*60)
    print(f"Results: {valid_count} valid, {invalid_count} invalid")
    print("="*60)
    
    return 0 if invalid_count == 0 else 1


def test_validate_blocks():
    assert validate_target() == 0


def test_default_def_id():
    data = {
        "name": "test_block"
    }
    block = ScriptsBlock.model_validate(data)
    print(block.def_id)
    assert block.def_id == "test_block"



def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="""Validate YAML block files against the blocks.json schema.

Usage:
    python validateBlocks.py                     # Validate all YAML files in data/blocks/
    python validateBlocks.py <file_path>         # Validate a specific file
    python validateBlocks.py <directory_path>    # Validate all YAML files in a directory"""
    )
    parser.add_argument("target", nargs="?", default=DEFAULT_BLOCKS_DIR, 
                        help="Target file or directory to validate.")
    args = parser.parse_args()

    # Parse arguments
    target_path = Path(args.target)
    return validate_target(target_path)
    
    
if __name__ == "__main__":
    sys.exit(main())
