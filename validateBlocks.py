#!/usr/bin/env python3
"""
Validate YAML block files against the blocks.json schema.

Usage:
    python validateBlocks.py                     # Validate all YAML files in data/blocks/
    python validateBlocks.py <file_path>         # Validate a specific file
    python validateBlocks.py <directory_path>    # Validate all YAML files in a directory
    python validateBlocks.py --help              # Show this help message
"""

import json
import yaml
import sys
import os
from pathlib import Path
from jsonschema import validate, ValidationError, Draft7Validator
from typing import Any, List, Tuple

# Default paths
DEFAULT_BLOCKS_DIR = "data/blocks"
DEFAULT_SCHEMA_PATH = "schemas/blocks.json"

def load_schema(schema_path: str) -> dict:
    """Load the JSON schema from file."""
    with open(schema_path, 'r') as f:
        return json.load(f)

def load_yaml_file(file_path: str) -> dict:
    """Load a YAML file and return its contents."""
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)

def validate_file(file_path: str, schema: dict) -> Tuple[bool, List[str]]:
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

def get_yaml_files(path: str) -> List[str]:
    """Get all YAML files from a path (file or directory)."""
    path_obj = Path(path)
    
    if path_obj.is_file():
        if path_obj.suffix.lower() in ['.yaml', '.yml']:
            return [str(path_obj)]
        return []
    elif path_obj.is_dir():
        return sorted([str(f) for f in path_obj.glob("*.yaml")] + 
                     [str(f) for f in path_obj.glob("*.yml")])
    
    return []

def main():
    """Main validation function."""
    # Parse arguments
    if len(sys.argv) > 1:
        if sys.argv[1] in ['--help', '-h', 'help']:
            print(__doc__)
            return 0
        target_path = sys.argv[1]
    else:
        target_path = DEFAULT_BLOCKS_DIR
    
    # Check if project root is correct
    if not os.path.exists(DEFAULT_SCHEMA_PATH):
        print(f"Error: Schema not found at {DEFAULT_SCHEMA_PATH}")
        print("Please run this script from the project root directory.")
        return 1
    
    # Load schema
    try:
        schema = load_schema(DEFAULT_SCHEMA_PATH)
    except Exception as e:
        print(f"Error loading schema: {e}")
        return 1
    
    # Get files to validate
    if not os.path.exists(target_path):
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

if __name__ == "__main__":
    sys.exit(main())
