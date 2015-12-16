#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Sarfraz Kapasi'
SITENAME = 'Chez Sarfraz'
SITEURL = ''

PATH = 'content'
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'en'

THEME='themes/pelican-bootstrap3'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('', '#'),
#         ('', '#'),)

# Social widget
#SOCIAL = (('', '#'),
#          ('', '#'),)

DEFAULT_PAGINATION = False

PLUGIN_PATHS = ['plugins']
PLUGINS = ['tag_cloud']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}


