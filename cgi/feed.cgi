#!/usr/bin/env python
# -*- coding: utf-8 -*-

import feedparser
import json

print("Content-type: application/json")
print("\n\n")

github = feedparser.parse("https://github.com/trileg.atom")
tech = feedparser.parse("https://tech.trileg.net/rss")
qiita = feedparser.parse("http://qiita.com/trileg/feed.atom")
response = {'github': github.entries, 'tech': tech.entries, 'qiita': qiita.entries}

print(json.JSONEncoder().encode(response))
print("\n")
