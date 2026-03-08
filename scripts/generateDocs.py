#!/usr/bin/env python3
"""
Auto-generates Sphinx documentation from YAML block definitions.
"""

import os
import sys
import yaml
from pathlib import Path
from typing import Dict, List, Any, Optional

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


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
        self.blocks: Dict[str, Any] = {}
        
    def load_blocks(self) -> None:
        """Load all block definitions from YAML files."""
        yaml_files = sorted(self.blocks_dir.glob('*.yaml'))
        
        for yaml_file in yaml_files:
            try:
                with open(yaml_file, 'r') as f:
                    block_data = yaml.safe_load(f)
                    if block_data and 'name' in block_data:
                        # if block_data['name'].startswith('_'):
                        #     continue
                        self.blocks[block_data['name']] = block_data
            except Exception as e:
                print(f"Warning: Failed to load {yaml_file}: {e}")
    
    def _format_description(self, text: Optional[str]) -> str:
        """Format description text for RST."""
        if not text:
            return ""
        # Remove extra whitespace and format
        return text.strip()
    
    def _generate_parameters_section(self, parameters: List[Dict[str, Any]]) -> str:
        """Generate RST documentation for parameters."""
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
                rst += f"   {description}\n\n"
            
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
    
    def _generate_id_section(self, id_info: Dict[str, Any]) -> str:
        """Generate RST documentation for ID properties."""
        if not id_info:
            return ""
        
        rst = "\nID Properties\n-------------\n\n"
        
        as_type = id_info.get('asType', False)
        if as_type:
            rst += "The ID of this block counts as the block type.\n\n"
        
        values = id_info.get('values', [])
        if values:
            rst += "**Allowed ID Values:**\n\n"
            for value in values:
                rst += f"- ``{value}``\n"
            rst += "\n"
        
        parents_without = id_info.get('parentsWithout', [])
        if parents_without:
            rst += "**Incompatible Parents:**\n\n"
            for parent in parents_without:
                rst += f"- {parent}\n"
            rst += "\n"
        
        return rst
    
    def _generate_hierarchy_section(self, block_data: Dict[str, Any]) -> str:
        """Generate RST documentation for block hierarchy."""
        rst = "\nHierarchy\n---------\n\n"
        
        should_have_parent = block_data.get('shouldHaveParent', False)
        if should_have_parent:
            parents = block_data.get('parents', [])
            if parents:
                rst += "**Valid Parent Blocks:**\n\n"
                for parent in parents:
                    rst += f"- :doc:`{self._get_block_link(parent)}`\n"
                rst += "\n"
            else:
                rst += "This block should have a parent block.\n\n"
        else:
            rst += "This block does not require a parent block.\n\n"
        
        needs_children = block_data.get('needsChildren', [])
        if needs_children:
            rst += "**Required Child Blocks:**\n\n"
            for child in needs_children:
                rst += f"- :doc:`{self._get_block_link(child)}`\n"
            rst += "\n"
        
        return rst
    
    def _get_block_link(self, block_name: str) -> str:
        """Get the documentation link for a block."""
        # Handle component blocks with IDs
        if block_name.startswith('component '):
            return block_name.lower().replace(' ', '_')
        return block_name.lower().replace(' ', '_')
    
    def generate_block_doc(self, block_name: str, block_data: Dict[str, Any]) -> str:
        """
        Generate RST documentation for a single block.
        
        Args:
            block_name: Name of the block
            block_data: Block definition data
            
        Returns:
            RST formatted documentation string
        """
        safe_name = self._get_block_link(block_name)
        
        # Header
        rst = f"{block_name}\n"
        rst += "=" * len(block_name) + "\n\n"
        
        # Description
        description = self._format_description(block_data.get('description', 'No description available.'))
        rst += f"{description}\n\n"
        
        # Hierarchy section
        rst += self._generate_hierarchy_section(block_data)
        
        # ID Properties section
        id_info = block_data.get('ID', {})
        if id_info:
            rst += self._generate_id_section(id_info)
        
        # Soft override info
        if block_data.get('softOverride', False):
            rst += "This block can be soft overridden in scripts.\n\n"
        
        # Parameters section
        parameters = block_data.get('parameters', [])
        rst += self._generate_parameters_section(parameters)
        
        return rst
    
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
            rst += f"   {safe_name}\n"
        
        return rst
    
    def write_documentation(self) -> None:
        """Write generated documentation to files."""
        # Create blocks index
        index_rst = self.generate_blocks_index()
        index_path = self.output_dir / 'index.rst'
        with open(index_path, 'w') as f:
            f.write(index_rst)
        print(f"Created {index_path}")
        
        # Create individual block files
        for block_name, block_data in self.blocks.items():
            doc_content = self.generate_block_doc(block_name, block_data)
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
