import json

with open('data.json') as json_file:
    data = json.load(json_file)

    print(data[0]['name'])

    name = data[0]['name']
    next = data[0]['la']
    prev = data[0]['second']

    person = {
        'name' : name,
        'next' : next,
        'prev' : prev
    }

print(person)