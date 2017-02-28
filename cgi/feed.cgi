#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import feedparser
import json

print("Content-type: application/json")
print("\n\n")

github = feedparser.parse("https://github.com/trileg.atom")
blog = feedparser.parse("https://blog.trileg.net/rss")
qiita = feedparser.parse("http://qiita.com/trileg/feed.atom")
response = {'github': github.entries, 'blog': blog.entries, 'qiita': qiita.entries}

print(json.JSONEncoder().encode(response))
print("\n")
