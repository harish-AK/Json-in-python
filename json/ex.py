'''Python	JSON
dict	Object
list	Array
tuple	Array
str	String
int	Number
float	Number
True	true
False	false
None	null
'''

import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

# convert into JSON:
#json load=json dumb
y = json.dumps(x)

# the result is a JSON string:
print(y)


print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))



#json fromat

x={"name": "John", "age": 30,
   'fruits':"apple",
   'cars':[{'model':'audi','second model':'bmw'}]

}
print(json.dumps(x,indent=4,separators=(".","=")))

#in sort format

print(json.dumps(x, indent=4, sort_keys=True))



# Define a dictionary
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Open file for writing
with open('output_file.json', 'w') as f:
    # Convert dictionary to JSON string with indentation and write to file
    json.dump(my_dict, f, indent=4)

with open('output_file2.json', 'w') as f:
    # Convert dictionary to JSON string with indentation and write to file
    json.dump(x, f, indent=4)

