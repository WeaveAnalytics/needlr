# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'needlr'
copyright = '2025, Tonio Lora, Tim Brown, Emily Nguyen, Bret Myers, Will Johnson'
author = 'Tonio Lora, Tim Brown, Emily Nguyen, Bret Myers, Will Johnson'
release = '0.2.1'

## -- Set Path -----------------------------------------------------
import os
import sys

sys.path.insert(0, os.path.abspath('../..'))

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.duration',
              'sphinx.ext.doctest',
              'sphinx.ext.autodoc',
              'sphinx.ext.autosummary']

autodoc_default_options = {
    "members": True,
    "undoc-members": False,
    "private-members": True,
}

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
