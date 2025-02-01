# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'doc-trial'
copyright = '2025, prithviraj'
author = 'prithviraj'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']


import os

# Use Read the Docs-specific output directory
if os.environ.get('READTHEDOCS'):
    html_output_dir = os.environ.get('READTHEDOCS_OUTPUT', '_build/html')
    html_output_dir = os.path.abspath(html_output_dir)
    html_static_path = [html_output_dir]