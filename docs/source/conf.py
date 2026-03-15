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

html_theme_options = {
    'collapse_navigation': False,
    'navigation_depth': 10,
    "external_links": [
        {"name": "ZedScripts", "url": "https://pzwiki.net/wiki/ZedScripts"},
    ],
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/SirDoggyJvla/pz-scripts-data",
            "icon": "fa-brands fa-github",
            "type": "fontawesome",
        },
        # {
        #     "name": "ZedScripts",
        #     "url": "https://pzwiki.net/wiki/ZedScripts",
        #     "icon": "https://raw.githubusercontent.com/SirDoggyJvla/ZedScripts/refs/heads/main/images/pz-script.png",
        #     "type": "url",
        # },
   ]
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
