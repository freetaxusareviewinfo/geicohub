# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Project information -----------------------------------------------------

project = 'Geico Insurance Guide'
copyright = '2026, Independent Insurance Guide'
author = 'Insurance Information Desk'
release = '1.0.0'

# -- General configuration ---------------------------------------------------

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- HTML output settings ----------------------------------------------------

html_theme = 'alabaster'

html_title = "Geico Insurance Guide – Quotes, Claims & Geico Phone Number"

html_short_title = "Geico Insurance Help"

html_favicon = 'favicon.ico'

html_show_sourcelink = False

html_allow_unsafe = True

html_theme_options = {
    'show_powered_by': False,
    'description': 'Step-by-step guide to Geico insurance quotes, claims process, login help, and official phone number support.',
}

html_static_path = ['_static']
html_css_files = ['custom.css']
