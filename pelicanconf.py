#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Jake Trimble'
SITENAME = 'jakes_blog'
SITEURL = 'https://trimbljk.github.io'
DIRECT_TEMPLATES = ['categories', 'index']
PATH = 'content'
THEME = 'custom_theme'
TIMEZONE = 'America/New_York'
CSS_FILE = 'custom.css'
DEFAULT_LANG = 'en'
DELETE_OUTPUT_DIRECTORY = True
MENUITEMS = (('Home', '#'),
        ('About', '#'),
        )
INDEX_SAVE_AS = 'blogroll.html'
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
SOCIAL = (('Github', 'https://github.com/Trimbljk/'),
         ('LinkedIn', 'https://www.linkedin.com/in/jake-trimble/'),
         ('Twitter', 'http://jinja.pocoo.org/'),)

LINKS = (('Check This Out', 'https://www.espn.com'),
         ('Testing', 'https://www.espn.com'),
         ('Check This Out', 'https://www.espn.com'))
DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
