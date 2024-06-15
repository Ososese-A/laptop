import json 

json_string = '''
{
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
'''

data = json.loads(json_string)
data['test'] = True

new_json = json.dumps(data, indent=4, sort_keys=True)
print(data)