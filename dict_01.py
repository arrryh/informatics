# словари

person = {
    'name': 'John',
    'age': 18,
    'last_name': 'Johnson',
    #'addres': 'Durand, Michigan(MI), 48429 Mount Street'
    'addres': {
        'city': 'Durand',
        'state': 'Michigan(MI)',
        'zip': 48429,
        'street': 'Mount Street'
    },
    'phone': None,
}

print(
    'person', person,
)

# получение значений

print(
    'name', person.get('name'),
    'name: ', person['name'],
    # 'email: ', person['email'],
    'email: ', person.get('email', None),
)
#result:
#name: John name:  John email:  None

# получение только значений словаря
print(
    person.values()
)
#result: 
#dict_values(['John', 18, 'Johnson', {'city': 'Durand', 'state': 'Michigan(MI)', 'zip': 48429, 'street': 'Mount Street'}, None])

# получить только ключи
print(
    person.keys()
)

#result: 
#dict_keys(['name', 'age', 'last_name', 'addres', 'phone'])

# получение пар ключ-значение в виде кортежа
print(
    person.items()
)
#result:
#dict_items([('name', 'John'), ('age', 18), ('last_name', 'Johnson'), ('addres', {'city': 'Durand', 'state': 'Michigan(MI)', 'zip': 48429, 'street': 'Mount Street'}), ('phone', None)])

for k in person.items():
    print(k)

for k in person.values():
    print(k)

# добавление значения

person['birthday'] = '2005-06-14'
print(
    'person: ', person
)

person.setdefault('birthday', '2005-06-14')
print(
    'person', person
)

