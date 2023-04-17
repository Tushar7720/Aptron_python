# wap to demonstrate args and kwargs

har = ["a","b","c","d","e"]
user = {'name': 'chetan',"age": 31}

def print_names(*args, **kwargs):
    for item in args:
        print(item)
    for key,value in kwargs.items():
        print(key,value)


print_names(*har,**user)