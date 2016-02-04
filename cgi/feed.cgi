#!/usr/bin/env python
# -*- coding: utf-8 -*-

import feedparser
import json

print("Content-type: application/json")
print()

d = feedparser.parse("https://github.com/trileg.atom")
response = {'title': d.feed.title}

print(json.JSONEncoder().encode(response))
