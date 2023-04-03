#ways to define a dictionary

user = {'name': 'chetan',"age": 31}
user2 = dict(name = "chetan",age = 31)
user3 = {'name': 'chetan',
         "age": 31}
#how to add to dictionary
d = {}
d["name"]= " chetan"
d["age"]= 31

print(d.values())
print(d.keys())
print(d.items())