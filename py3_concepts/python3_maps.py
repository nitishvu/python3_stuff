'''
Python map() function is used to apply a function on all the elements
of specified iterable and return map object. 
Python map object is an iterator,so we can iterate over its elements.
We can also convert map object to sequence objects such as list, tuple etc. using their factory functions.

Syntax :

map( my_func, ,my_iter)

my_func :  function to which map passes each element of given iterable.
my_iter : iterable which is to be mapped.


'''

#Python map() with string

#iterable lets take a list
my_iter = [1, 2, 3, 4]

def my_func(item):
    return item * item
    
#Now we have both function(my_func) and iterable(my_iter)
#out put of map fucntion which is a map object we can use this 
#map object with list(),set().
print(map(my_func, my_iter)) 
print(list(map(my_func, my_iter)))
print(set(map(my_func, my_iter)))

'''

O/P:
<map object at 0x000001B2C2040A60>
[1, 4, 9, 16]
{16, 1, 4, 9}

'''

#Now lets try with number strings  to split the digits
#here we are using python 3 function list,tuple we can also use sets.

my_iter2 = ["346", "542", "134", "146"]
my_digit_list = list(map(list, my_iter2))
print(my_digit_list)

# here i am using tuple 
my_digit_set = set(map(tuple, my_iter2))
print(my_digit_list)
'''
O/P:
[['3', '4', '6'], ['5', '4', '2'], ['1', '3', '4'], ['1', '4', '6']]
[['3', '4', '6'], ['5', '4', '2'], ['1', '3', '4'], ['1', '4', '6']]
'''
