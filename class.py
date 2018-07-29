import numpy as np

print(1288)
print(639)
print(1288 + 639)
print((749 + 371 + 828 + 503 + 1379)/5)

sum = ((749 + 371 + 828 + 503 + 1379)/5)
print("sum = %d" %sum)

aaa = 749
ana = 371
bna = 828
cna = 503.876
dna = 1379

print(ana)
print(cna)

a_string = "Abdullah"
a_float = 1379.5
a_int = 13

print(type(a_string))
print(type(a_float))
print(type(a_int))

cities = []
cities.append("mama")
cities.append("nana")
cities.append("caca")
cities.append("kaka")
cities.append("ababa")

print(cities)

myList = [1, 2, 3, 4, 5]

myList2 = [5, 6, 7]

myList3 = ["apple", "banana", "cherry"]

print(myList[1])

print(len(myList) + len(myList2))

print(myList[1:4])

print(myList[2:])

print(myList[:3])

a = len(myList)
b = len(myList)-2

slice_m = myList[b:a]
print(slice_m)

myList[2] = 201

myList[0:3] = [15, 25, 35]

print(myList)

del(myList[0:3])

print(myList)

x = [1, 2, 3]
y = x + [4, 5, 6]

print(y)

print(x)

z = x
z[1] = 999

print(x)

print(z)

x = [1, 2, 3]
z = list(x)
z = x[:]
z[1] = 555

print(z)

print(x)

height = [1.2, 2, 1.2, 2, 1, 2, 1, 2]
weight = [1, 22, 1, 2, 1, 22, 1, 2]
#cal = weight/height**2

np_height = np.array(height)
np_weight = np.array(weight)

bmi = np_weight/np_height**2

print(bmi)

h = np.array([1, 2, 3])

s = x + h  # addition two list elements

print(s)

p = x + x  # just show two list beside

print(p)


print(bmi > 2)  # return all true or false
print(bmi[bmi > 2])  # return true values

np_2d = np.array([[1, 2, 53], [5, 6, 7]])

print(np_2d.shape)

print(np_2d[:, 1:3])

print(np_2d[1:])

x = [4, 1, 2, 3]
x.sort()
print(x)

ss = "a\nb\nc"
ssss = ss.split("\n")
print(ssss)

f = open('my.csv', 'r')
data = f.read()
print(data)

rows = data.split('\n')
print(rows[0:1])

'''

'''


