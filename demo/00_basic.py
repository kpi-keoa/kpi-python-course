people = {
    'Молодой': 14,
    'Старый':  8.5,
    "Сложный": [20, 1 + 8j]
}

people.update({i * 'BLAH ': i for i in range(10)})

print(people)

from pprint import pprint
print('PRETTY:')
pprint(people)
