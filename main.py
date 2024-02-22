# print('Hello', 'World!')

print('Hello', '\tWorld! \n')  # print('Hello', 'World!')
print('Hello', 'World!')  # print('Hello', 'World!')
print('Hello', 'World!')  # print('Hello', 'World!')

# print('Hello', 'World!')
print(
    'Hello', 
    'World!'
    )  

if 3 > 2:
    print('Yes, 3 > 2')
    if 3 < 4:
        print('but 3 < 4')


print('Hello, John!')

# print numbers of 0 to 10
# for i in range(10):
    # print(i)

a = 1
b = 2
c = 5.6

s = 'Hello John!'

print(a, b, c, s)

a = 'aaaa'

print('a:', type(a))
print('b:', type(b))
print('c:', type(c))
print('s:', type(s))

b = float(b)
c = str(c)
d = int(2.9999999999999999)

print('b:', type(b), b)
print('c:', type(c), c)
print('d:', type(d), d)

print(a is b)  #сравнение типов данных переменных

l= [1, 2, 3, 'b', 'c', 5.2]
print(l)

print(l[0])

print(len(l)) #длина массива

print(l[len(l)-1])

l.append('asdasd') #добавить элемент в конец списка
print(l)

def sum(a, b):
    # first solution
    # if type(a) == str or type(b) is str:
    #    return 0
    # else:
    #    return a + b
    
    #second solution
    if type(a) != float or type(a) != int:
        return 0
    
    if type(b) != float or type(b) != int:
        return 0
    
e = sum(5, 9)
print('SUM:', e)

if 1 > 2:
    print('1 > 2')
else:
    print('2 > 1')

if 1 > 2:
    print('1 > 2')
elif 1 > 0.5:
    print('1 > 0.5')
else:
    print('1 < 2 and 1 < 0.5')


result = sum(1, '2')
print(result)

def foo(a):
    print('a: ', a)    #вывести весь массив
    a.append('111111111111')
    a.append('2222')
foo(l)

print('List: ', l)

def fool(a):
    a = 333

fool(b)
print(b)

#словарь
f = {
    'a': 100,
    'b': 200,
    'c': 250,
}
print(type(f))

print(f)
