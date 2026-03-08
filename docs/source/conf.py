# Configuration file for the Sphinx documentation builder.

import os
import sys

# Add parent directory and docs directory to path
sys.path.insert(0, os.path.abspath('../../'))
sys.path.insert(0, os.path.abspath('../'))

project = 'Project Zomboid Scripts API Reference'
copyright = '2026, Scripts-Data Contributors'
author = 'Scripts-Data Contributors'
release = '1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_title = 'Project Zomboid Scripts API Reference'
html_logo = None
html_favicon = None

# Sphinx RTD Theme options
html_theme_options = {
    # 'logo_only': False,
    # 'prev_next_buttons_location': 'bottom',
    # 'style_external_links': False,
    # 'vcs_pageview_mode': '',
    # 'style_nav_header_background': '#2980B9',
    'collapse_navigation': True,
    # 'sticky_navigation': True,
    'navigation_depth': 4,
    # 'includehidden': True,
    # 'titles_only': False,
    "external_links": [
        {"name": "Repository", "url": "https://github.com/SirDoggyJvla/pz-scripts-data"},
        {"name": "ZedScripts", "url": "https://pzwiki.net/wiki/ZedScripts"},
    ],
}

# LaTeX output options
latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '10pt',
}

# Output for man pages
man_pages = [
    ('index', 'scripts-api', 'Project Zomboid Scripts API Reference',
     ['Scripts-Data Contributors'], 1)
]
