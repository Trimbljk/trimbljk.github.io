#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Jake Trimble'
SITENAME = 'Just Another Data Science Blog'
SITE_URL = 'https://trimbljk.github.io'
DIRECT_TEMPLATES = ['index', 'archives']
PATH = 'content'
THEME = 'custom_theme'
TIMEZONE = 'America/New_York'
CSS_FILE = 'custom.css'
DEFAULT_LANG = 'en'
DELETE_OUTPUT_DIRECTORY = True
MENUITEMS = (('Home', 'https://trimbljk.github.io'),
        ('About', 'https://trimbljk.github.io'),
        ('Data Science', 'https://trimbljk.github.io/data-science.html'),
        ('Programming', 'https://trimbljk.github.io/programming.html'),
        ('Musings', 'https://trimbljk.github.io/musings.html'),
        ('Archives', 'https://trimbljk.github.io/archives.html'),
        )
INDEX_SAVE_AS = 'all/blogroll.html'
ARTICLE_SAVE_AS = 'article/{slug}/index.html'
SUMMARY_MAX_LENGTH = 15
DEFAULT_DATE_FORMAT = '%Y-%B-%d'
RELATIVE_URLS = False
CATEGORY_SAVE_AS = '{slug}.html'
CATEGORY_URL = 'category/{slug}.html'
DISPLAY_CATEGORIES_ON_MENU = False
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
