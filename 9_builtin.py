import html.parser
import urllib.request
from collections import defaultdict


class MyHTMLParser(html.parser.HTMLParser):
    def __init__(self) -> None:
        self.tag_count = defaultdict(int)
        self.tags_with_attrs_count = defaultdict(int)
        super().__init__()

    def handle_starttag(self, tag, attrs):
        self.tag_count[tag] += 1
        if attrs:
            self.tags_with_attrs_count[tag] += 1


parser = MyHTMLParser()

with urllib.request.urlopen("https://jetlend.ru/") as data:
    parser.feed(data.read().decode("utf-8"))

total_tags = 0
total_tags_with_attrs = 0

print("TAG COUNT:")
for key, value in parser.tag_count.items():
    print(f"{key}: {value}")
    total_tags += value
print(f"TOTAL TAG COUNT = {total_tags}")

print("_____________")

print("TAGS WITH ATTRIBUTES COUNT:")
for key, value in parser.tags_with_attrs_count.items():
    print(f"{key}: {value}")
    total_tags_with_attrs += value
print(f"TOTAL TAG WITH ATTRIBUTES COUNT = {total_tags_with_attrs}")

print("_____________")

print(f"TAGS: {total_tags}\nTAGS WITH ATTRS: {total_tags_with_attrs}")
