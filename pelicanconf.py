#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'ackrep-team'
SITENAME = 'ACKREP – Automatic Control Knowledge Repository'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


# everything below is manually specified after `pelican quicstart`
# *******

from datetime import datetime

THEME = 'themes/ackrep-standard'


OUTPUT_PATH = 'docs/'

# these paths are relative to /content
STATIC_PATHS = ["downloads", "img"]

JINJA_GLOBALS = {
"BUILD_TIME": datetime.utcnow()

}


# source:  https://github.com/getpelican/pelican/issues/1357#issuecomment-362075129
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc': {},
    },
    'output_format': 'html5',
}


# suppress generation of unnecessary blog overview files
TAGS_SAVE_AS = ""
ARCHIVES_SAVE_AS = ""
AUTHORS_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""
