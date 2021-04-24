import json

with open('real.json', 'r') as read:
    annotations = json.load(read)

print((annotations['annotations'][0].keys()))
