# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# To read environment variables:
import os
import datetime

# -- Project information -----------------------------------------------------

copyright = u'{0} Inrupt Inc.'.format(datetime.date.today().year)

# -- General configuration ---------------------------------------------------


# -- product name -----
# -- Separately update code samples and toc links and docs-navbar since not using substitutions--

name = 'PodBrowser'

pygments_style = 'sphinx'

# -- Using .txt instead of .rst for restructured text -----------------------
source_suffix = {
    '.rst': 'restructuredtext',
}

# -- Add lexers
from sphinx.highlighting import lexers

highlight_language = 'javascript'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.extlinks',
    'sphinx.ext.todo',
]

# Staring in 2.0, sphinx_tabs collapses when double-clicked
# Disabling the collapse behavior

sphinx_tabs_disable_tab_closing = True 
extlinks = {
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['./build/docs-assets/_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['includes']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'

html_theme = 'inrupt'
html_theme_path = ['./build/docs-assets/themes']

html_copy_source = False

html_title = 'Inrupt {0}'.format(name)

html_favicon = "https://docs.inrupt.com/inrupt_stickers_v2-03.png"

# These theme options are declared in ./themes/inrupt/theme.conf
# as well as some for pydata_sphinx_theme


html_theme_options = {
    'project_title': 'Inrupt {0}'.format(name),
    'banner': True,
    'banner_msg': 'PodBrowser has been deprecated as of Feb 27, 2023.',
    'robots_index': True,
    'github_editable': False,
    'docs_project': 'user-interface/podbrowser',
    
    # below are pydata_sphinx_theme
    "footer_start": [ "copyright.html"],
    "footer_end": [ ],
    "navbar_align": "left",
    "icon_links": [
        {
            "name": "Support Desk",
            "url": "https://inrupt.atlassian.net/servicedesk",
            "icon": "fas fa-tools",
        },
        {
            "name": "Solid forum",
            "url": "https://forum.solidproject.org/",
            "icon": "fas fa-users",
        },
        {
            "name": "Inrupt Blog",
            "url": "https://inrupt.com/blog",
            "icon": "fas fa-blog",
        },
    ],

}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['./build/docs-assets/_static']
html_css_files = [
    'css/inrupt.css',
]

html_sidebars = {
    '**': [ 'search-field.html',  'docs-sidebar.html'],
}

html_context = {
   "default_mode": "auto"
}

locale_dirs = ['locale/']   # path is example but recommended.
gettext_compact = False     # optional.
