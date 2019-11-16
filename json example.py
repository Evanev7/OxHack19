import json

with open("example.json") as file:
    data = json.load(file)

print(data)
