# load

# import json

# data='{"name": "Anu","age": 25,"isStudent": true,"Skills": ["Python", "SQL"],"Address": {"city":"Mumbai","pincode": 400001 }}'
# list_of_data=json.loads(data)
# print(list_of_data)
# print(list_of_data["Address"]["city"])
# print(list_of_data["Skills"][1])

# dump

import json
dictio={"name": "Anu","age": 25,"isStudent": True,"Skills": ["Python", "SQL"],"Address": {"city":"Mumbai","pincode": 400001 }}
a = json.dumps(dictio)
print(a)
print(str(a))


import json
import requests
# Step 1: Make a GET request to the API
response = requests.get("https://randomuser.me/api/")
# Step 2: Convert response JSON → Python dict
data = response.json()
# Step 3: Extract some values
user = data["results"][0]
name = user["name"]["first"]
email = user["email"]
city = user["location"]["city"]
print("Name:", name)
print("Email:", email)
print("City:", city)