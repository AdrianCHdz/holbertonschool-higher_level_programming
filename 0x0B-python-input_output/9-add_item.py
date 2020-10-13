#!/usr/bin/python3
"""docs for module"""


from sys import argv

save_json = __import__('7-save_to_json_file').save_to_json_file
load_json = __import__('8-load_from_json_file').load_from_json_file
filename = "add_item.json"

with open(filename, 'a+') as f:
    pass

content = []
try:
    content = load_json(filename)
except Exception:
    pass
args = argv[1:]
content += args
save_json(content, filename)
