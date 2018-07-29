import numpy as np
import pandas as pd

dic1 = {2:10, 1:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}


dic1.update(dic2)
dic1.update(dic3)

print(dic1)


#################################################################


d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

def noman_func(x):
    for key, value in enumerate(d):
        if value in d:
            print('Value is present in the dictionary')
        else:
            print('Value is not present in the dictionary')

noman_func(30)


#################################################################
'''
A lambda is an anonymous function:

>>> f = lambda: 'foo'
>>> print f()
foo

'''

my_dict = {'x': 600, 'y': 874, 'z': 560}

key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))

print('Maximum Value: ', my_dict[key_max])
print('Minimum Value: ', my_dict[key_min])

#################################################################

from collections import Counter

# A Counter is a container that keeps track of how many times equivalent values are added.


d1 = {'a': 300, 'b': 300, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

d = Counter(d1) + Counter(d2)

print(d)


#################################################################



sam_list = [[1, 2, 3, 4, 5, 6]]

myarray = np.asarray(sam_list)

print(myarray)

print(myarray[0:2])
print(myarray[2:4])
print(myarray[4:])



np_2d = np.array(sam_list)

print(np_2d.shape)

#################################################################

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
             'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
             'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
             'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
             }



my_data = pd.DataFrame(exam_data)

print(my_data)


row_labels = ['a', 'b', 'c', 'd', 'e',  'f',  'g',  'h',  'i',  'j']

my_data.index = row_labels

print(my_data)


#################################################################

my_data = pd.read_csv('exam_data.csv')

print(my_data)

my_data = pd.read_csv('exam_data.csv', index_col=0)

print(my_data)