#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
import json

print("Content-type: application/json")
print("\n\n")

birthday = datetime.strptime("1993-03-14", "%Y-%m-%d")
today = datetime.today()

age = today.year - birthday.year \
      - ((today.month, today.day) < (birthday.month, birthday.day))

response = {'age': age}

print(json.JSONEncoder().encode(response))
print("\n")
