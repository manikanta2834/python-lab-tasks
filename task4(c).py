dictionary={'name': 'Mani', 'age': 19, 'city': 'india'}
print(dictionary)

print(dictionary['name'])
print(dictionary['age'])


dictionary['name']= "sai"
print(dictionary)
dictionary.pop('city')
print(dictionary)

for k in dictionary:
    print("KEY:",k)

print(dictionary.items())