#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import secrets
import string
import json

print("Content-type: application/json")
print("\n\n")

rnd_word_length = 8

alphabet = string.ascii_letters + string.digits
while True:
  rnd_word = ''.join(secrets.choice(alphabet) for i in range(rnd_word_length))
  if (any(c.islower() for c in rnd_word) and any(c.isupper() for c in rnd_word) and sum(c.isdigit() for c in rnd_word) >= 2):
    break

response = {'rnd_word': rnd_word}

print(json.JSONEncoder().encode(response))
print("\n")
