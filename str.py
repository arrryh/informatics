# Операции со строками

s = "Lorem \tIpsum is simply dummy text of the printing and typesetting industry. \n Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."
print(s)

# первый символ строки
print(s[0])

# длина строки
print('len str: ', len(s))   

print(s[len(s)-1]) # or print(s[-1]) - последний символ строки

print(s[-5])

# вывод первых 10 символов строки
print(s[:10])

# срез начиная с 10 символа из 20 символов (с 10 по 30)
print(s[10:30])

#срез каждого третьего символа с 10 по 20
print(s[10:20:3])

#каждый третьй символ во всей строке
print(s[::3])

# не сработает, т.к. строка - неизменяемый тип данных
# s[0] = 'adasad'

#конкатенация строк
s1 = '11111' + 'as das dasd'
print(s1)

#заменить первый символ в строке s на строку s1
s = s1 + s[1:]
print(s)

#соединение списка в строку с разделителем ', '
l = ['Lorem', 'Ipsum', 'is', 'simply', 'dummy', 'of']
s2 = ', '.join(l)
print(s2)

#создание списка из строки по символу '.' - разбиение по предложениям
l2 = s.split('.')
print(l2)

#удаление пробелов с начала строки и с конца
s3 = ' Hello, John! '
print(s3, 'len: ', len(s3))
s3 = s3.lstrip()
print(s3, 'len: ', len(s3))
s3 = s3.rstrip()
print(s3, 'len: ', len(s3))

#смена регистра строки
s4 = 'nam libero'
print(s4.upper())
s5 = 'LOREM IPSUM'
print(s5.lower())


#задача перевода первой буквы строки в верхний регистр, а остальных в нижний
s6 = 'lorem ipsum dolor sit amet, consectetur adipiscing elit'
print(s6.capitalize())
# Lorem ipsum dolor sit amet, consectetur adipiscing elit

#второй вариант
s61 = s6[:1]
s61 = s61.upper()
s6 = s61 + s6[1:]
print(s6)

