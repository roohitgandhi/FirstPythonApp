# import function_modules as m
# import math
# import requests

# # res = math.sqrt(9)
# # print(res)
# # print(math.pi) 

# # mixed = [5, "test", 10]
# # mixed.append("something New appended")
# # print(mixed)

# # acronyms = {
# #     'kkk': 'val1',
# #     2: 'val2'
# # }
# # print(acronyms[2])

# res = requests.get('http://api.open-notify.org/astros.json')
# print(res.json())

class Robot_Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def bark(self):
        print('bau bau')

mydog = Robot_Dog('dog01', 'Pomerian')
print(mydog.name)
mydog.bark()