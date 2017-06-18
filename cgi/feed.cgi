#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import feedparser
import json

print("Content-type: application/json")
print("\n\n")

github = feedparser.parse("https://github.com/k3nsuk3.atom")
blog = feedparser.parse("https://blog.k3n.link/rss")
qiita = feedparser.parse("http://qiita.com/k3nsuk3/feed.atom")
response = {'github': github.entries, 'blog': blog.entries, 'qiita': qiita.entries}

print(json.JSONEncoder().encode(response))
print("\n")
