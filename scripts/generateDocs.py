#!/usr/bin/env python3
"""
Auto-generates Sphinx documentation from YAML block definitions.
"""

import os
import sys
import yaml
from m2r import convert
from pathlib import Path
from typing import Dict, List, Any, Optional

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def _get_block_link(block_name: str) -> str:
    """Get the documentation link for a block."""
    return block_name.lower().replace(' ', '_')


def _dict_to_rst_csv(data: Dict[str, Any]) -> str:
    """Convert a dictionary to an RST CSV table."""
    rst = ".. csv-table::\n"
    rst += "   :header: " + ", ".join(f'"{key}"' for key in data.keys()) + "\n"
    rst += "   :widths: " + ", ".join("20" for _ in data) + "\n\n"
    
    # Add the single row of data
    rst += "   " + ", ".join(f'"{value}"' for value in data.values()) + "\n\n"
    
    return rst



children_map = {}
class ScriptBlock:
    """Represents a script block definition."""
    
    def __init__(self, name: str, data: Dict[str, Any]):
        self.name = name
        self.data = data

    def _format_description(self, text: Optional[str]) -> str:
        """Format the block description for RST."""
        if not text:
            return ""
        # Remove extra whitespace and format
        return convert(text).strip()
    
    def _generate_properties_table(self) -> str:
        properties = {
            "Parent blocks": ", ".join(self.data.get('parents', [])) if self.data.get('parents') else "None",
            "Required child blocks": ", ".join(self.data.get('needsChildren', [])) if self.data.get('needsChildren') else "None",
            "Possible child blocks": ", ".join(children_map.get(self.name, [])) if children_map.get(self.name) else "None",
            "Soft Override": "Yes" if self.data.get('softOverride', False) else "No",
        }
        return _dict_to_rst_csv(properties)
    
    def _generate_hierarchy_section(self) -> str:
        """Generate RST documentation for block hierarchy."""
        block_data = self.data
        
        rst = "\nHierarchy\n---------\n\n"
        block_name = block_data.get('name', '')
        
        should_have_parent = block_data.get('shouldHaveParent', False)
        if should_have_parent:
            parents = block_data.get('parents', [])
            if parents:
                rst += "**Valid Parent Blocks:**\n\n"
                for parent in parents:
                    rst += f"- :doc:`{_get_block_link(parent)}`\n"
                rst += "\n"
            else:
                rst += "This block should have a parent block.\n\n"
        else:
            rst += "This block does not require a parent block.\n\n"
        
        needs_children = block_data.get('needsChildren', [])
        if needs_children:
            rst += "**Required Child Blocks:**\n\n"
            for child in needs_children:
                rst += f"- :doc:`{_get_block_link(child)}`\n"
            rst += "\n"
        
        # Show all possible child blocks
        possible_children = children_map.get(block_name, [])
        if possible_children:
            rst += "**Possible Child Blocks:**\n\n"
            # Sort and display all possible children
            for child in sorted(possible_children):
                rst += f"- :doc:`{_get_block_link(child)}`\n"
            rst += "\n"
        
        return rst
    
    def _generate_id_section(self) -> str:
        """Generate RST documentation for ID properties."""

        rst = "\nID Properties\n-------------\n\n"

        id_info: dict|None = self.data.get('ID', None)
        if id_info is None:
            rst += "This block should not have an ID.\n\n"
            return rst

        rst += "This block should have an ID.\n\n"
        
        as_type = id_info.get('asType', False)
        values = id_info.get('values', [])
        if as_type:
            rst += "Using a specific ID will make this block have different properties.\n\n"
            # for value in values:
            #     rst += f"- :doc:`{value} <{self._get_block_link(f"{block_name} {value}")}>`\n"
            # rst += "\n"
        
        if values:
            rst += "**Allowed ID Values:**\n\n"
            for value in values:
                if as_type:
                    rst += f"- :doc:`{value} <{_get_block_link(f"{self.name} {value}")}>`\n"
                else:
                    rst += f"- ``{value}``\n"
            rst += "\n"
        
        parents_without = id_info.get('parentsWithout', [])
        if parents_without:
            rst += "**Incompatible Parents:**\n\n"
            for parent in parents_without:
                rst += f"- {parent}\n"
            rst += "\n"
        
        return rst
    
    def _generate_parameters_section(self) -> str:
        """Generate RST documentation for parameters."""
        parameters = self.data.get('parameters', None)
        if not parameters:
            return ""
        
        rst = "\nParameters\n----------\n\n"
        
        for param in parameters:
            name = param.get('name', 'Unknown')
            description = self._format_description(param.get('description', 'No description'))
            param_type = param.get('type', 'Any')
            required = param.get('required', False)
            default = param.get('default')
            
            # Parameter name as definition
            rst += f"**{name}**\n"
            
            # Type and required status
            type_info = f"Type: ``{param_type}``"
            if required:
                type_info += " *(required)*"
            rst += f"   {type_info}\n\n"
            
            # Description
            if description:
                indented_description = "\n   ".join(description.split("\n"))
                rst += f"   {indented_description}\n\n"
            
            # Default value if present
            if default is not None and default != "":
                if isinstance(default, list):
                    default_str = ", ".join(str(v) for v in default) if default else ""
                else:
                    default_str = str(default)
                if default_str:  # Only show if non-empty
                    rst += f"   Default: ``{default_str}``\n\n"
            
            # Additional attributes
            if param.get('allowedDuplicate'):
                rst += "   Can be duplicated: ✓\n\n"
            if param.get('canBeEmpty'):
                rst += "   Can be empty: ✓\n\n"
            
            item_types = param.get('itemTypes', [])
            if item_types:
                types_str = ", ".join(item_types)
                rst += f"   Item types: {types_str}\n\n"
            
            parents_only = param.get('parentsOnly', [])
            if parents_only:
                parents_str = ", ".join(parents_only)
                rst += f"   Only for parents: {parents_str}\n\n"
        
        return rst

    def generate_doc(self) -> str:
        """Generate RST documentation for this block."""
        # Header
        rst = f"{self.name}\n"
        rst += "=" * len(self.name) + "\n\n"

        # Description
        description = self._format_description(self.data.get('description', 'No description available.'))
        rst += f"{description}\n\n"

        # rst += self._generate_properties_table()

        # Soft override info
        if self.data.get('softOverride', False):
            rst += "This block can be soft overridden in scripts.\n\n"

        # Hierarchy section
        rst += self._generate_hierarchy_section()

        # ID Properties section
        rst += self._generate_id_section()

        # Parameters section
        rst += self._generate_parameters_section()

        return rst



class BlockDocumentationGenerator:
    """Generates RST documentation from YAML block definitions."""
    
    def __init__(self, blocks_dir: Path, output_dir: Path):
        """
        Initialize the generator.
        
        Args:
            blocks_dir: Path to the blocks directory
            output_dir: Path to output documentation directory
        """
        self.blocks_dir = blocks_dir
        self.output_dir = output_dir
        self.blocks: Dict[str, ScriptBlock] = {}

    def load_blocks(self) -> None:
        """Load all block definitions from YAML files."""
        yaml_files = sorted(self.blocks_dir.glob('*.yaml'))
        
        for yaml_file in yaml_files:
            try:
                with open(yaml_file, 'r') as f:
                    block_data: dict = yaml.safe_load(f)
                    if block_data and 'name' in block_data:
                        # if block_data['name'].startswith('_'):
                        #     continue
                        self.blocks[block_data['name']] = ScriptBlock(block_data['name'], block_data)
            except Exception as e:
                print(f"Warning: Failed to load {yaml_file}: {e}")
        
        # Build children map after all blocks are loaded
        self._build_children_map()
    
    def _build_children_map(self) -> None:
        """Build a map of which blocks can be children of which parent blocks."""
        for block_name, block in self.blocks.items():
            parents = block.data.get('parents', [])
            for parent in parents:
                if parent not in children_map:
                    children_map[parent] = []
                children_map[parent].append(block_name)

    def _get_block_link(self, block_name: str) -> str:
        """Get the documentation link for a block."""
        return block_name.lower().replace(' ', '_')
    
    def generate_blocks_index(self) -> str:
        """Generate the blocks index RST file."""
        rst = "Script Blocks Reference\n"
        rst += "=" * len("Script Blocks Reference") + "\n\n"
        rst += "This section provides detailed documentation for all available script blocks.\n\n"
        rst += ".. toctree::\n"
        rst += "   :maxdepth: 1\n"
        rst += "   :caption: Blocks\n\n"
        
        # Sort blocks by name
        for block_name in sorted(self.blocks.keys(), key=str.lower):
            safe_name = self._get_block_link(block_name)
            rst += f"   blocks/{safe_name}\n"
        
        return rst
    
    def write_documentation(self) -> None:
        """Write generated documentation to files."""
        # Create blocks index
        index_rst = self.generate_blocks_index()
        index_path = os.path.join(os.path.dirname(self.output_dir), 'blocks.rst')
        with open(index_path, 'w') as f:
            f.write(index_rst)
        print(f"Created {index_path}")
        
        # Create individual block files
        for block_name, block in self.blocks.items():
            doc_content = block.generate_doc()
            safe_name = self._get_block_link(block_name)
            block_path = self.output_dir / f'{safe_name}.rst'
            
            with open(block_path, 'w') as f:
                f.write(doc_content)
            print(f"Created {block_path}")
    
    def run(self) -> None:
        """Execute the documentation generation."""
        print("Loading block definitions...")
        self.load_blocks()
        print(f"Loaded {len(self.blocks)} blocks")
        
        print("Generating documentation...")
        self.write_documentation()
        print("Documentation generation complete!")


def main():
    """Main entry point."""
    # Determine paths
    script_dir = Path(__file__).parent
    root_dir = script_dir.parent  # Go up from scripts to root
    blocks_dir = root_dir / 'data' / 'blocks'
    output_dir = root_dir / 'docs' / 'source' / 'blocks'
    
    # Verify paths exist
    if not blocks_dir.exists():
        print(f"Error: Blocks directory not found: {blocks_dir}")
        sys.exit(1)
    
    if not output_dir.exists():
        print(f"Error: Output directory not found: {output_dir}")
        sys.exit(1)
    
    # Generate documentation
    generator = BlockDocumentationGenerator(blocks_dir, output_dir)
    generator.run()


if __name__ == '__main__':
    main()
