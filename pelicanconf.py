#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'youngsterxyf'
SITENAME = u'\u4f17\u6210\u6280\u672f\u805a\u4e50\u90e8'
SITEURL = 'http://happytechgroup.github.io'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
# LINKS =  (('众成Github', 'https://github.com/HappyTechGroup'),)

# Social widget
SOCIAL = (('众成Github', 'https://github.com/HappyTechGroup'),
        ('众成Weibo', 'http://weibo.com/u/5232590998'),)

DEFAULT_PAGINATION = 10

THEME = 'my-octopress'

DATE_FORMATS = {
        'zh': '%Y-%m-%d %a'    
}
RELATIVE_URLS = True

DISQUS_SITENAME = 'happytechgroup'

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

DEFAULT_CATEGORY = u'其他'

PAGE_DIR = 'pages'
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

MENUITEMS = (
     (u'归档', '/archives.html'),
     (u'成员', '/pages/members.html'),
     (u'RSS', '/feeds/all.xml'),
)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
