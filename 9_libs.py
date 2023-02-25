import requests
from bs4 import BeautifulSoup
from collections import defaultdict

tag_count = defaultdict(int)
tags_with_attrs_count = defaultdict(int)

data = requests.get("https://jetlend.ru")
soup = BeautifulSoup(data.text, "html.parser")
for tag in soup.find_all():
    tag_count[tag.name] += 1
    if tag.attrs:
        tags_with_attrs_count[tag.name] += 1

total_tags = 0
total_tags_with_attrs = 0

print("TAG COUNT:")
for key, value in tag_count.items():
    print(f"{key}: {value}")
    total_tags += value
print(f"TOTAL TAG COUNT = {total_tags}")

print("_____________")

print("TAGS WITH ATTRIBUTES COUNT:")
for key, value in tags_with_attrs_count.items():
    print(f"{key}: {value}")
    total_tags_with_attrs += value
print(f"TOTAL TAG WITH ATTRIBUTES COUNT = {total_tags_with_attrs}")

print("_____________")

print(f"TAGS: {total_tags}\nTAGS WITH ATTRS: {total_tags_with_attrs}")
