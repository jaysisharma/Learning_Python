import json

# Creating a dictionary

data = {
    "name" : "Mike",
    "age":20,
    "gender" : "M"
}

# Writing on a json file

with open('data.json', 'w') as file:
    json.dump(data,file)


# Reading a json file
    
with open('data.json', 'r') as file:
    data = json.load(file) # Parsing the json file

    print(data)

