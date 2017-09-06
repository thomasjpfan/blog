#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://thomasjpfan.com'
RELATIVE_URLS = False
SHORTSITEURL = "thomasjpfan.com"

FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'

DELETE_OUTPUT_DIRECTORY = True

MENUITEMS = (('Rss', SITEURL + "/" + FEED_ALL_ATOM),)

# Following items are often useful when publishing

# DISQUS_SITENAME = "thomasjpfan"
GOOGLE_ANALYTICS = "UA-46065142-1"