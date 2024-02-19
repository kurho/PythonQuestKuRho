import json

with open('example2.json' , 'r') as file:
    data = json.load(file)

    out = json.dumps(data, indent=2)

    print(data)
