import json

mydict = {
    "people": [
        {
            "name" : "Bob",
            "age": 28,
            "weight" : 88
        },

        {
            "name": "Anna",
            "age" :34,
            "weight" : 67
        },

        {
            "name" : "Charles",
            "age" : 45,
            "weight" : 78
        },
        {
            "name" : "Daniel",
            "age": 21,
            "weight" : 110
        }
    ]
}

json_string = json.dumps(mydict,indent=2)
with open('mydata.json','w') as f:
    f.write(json_string)

#//////////////////////////////////////////////////////////////////////////////////////////////

with open('mydata.json','r') as f:
    json_object = json.loads(f.read())

print(json_object['people'][0]['name'])

with open('mydata.json','r') as file:
    json_item = json.loads(file.read())

print(json_item)

nine = {
            "name" : "Dan",
            "age": 21,
            "weight" : 110
        }

list(json_item).append(nine)

print(json_item)
