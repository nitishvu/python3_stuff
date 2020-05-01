'''
python 3 lambda syntax is simple

lambda argument_list: expression

The argument list consists of a comma separated list of arguments and the expression 
is an arithmetic expression using these arguments. 

you can assgin lambda function to variable as below


my_func = lambda argument_list: expression

'''

#example1:

sum = lambda a,b : a+b

'''
this is equals to below function
def sum(a,b):
    return a+b
'''
print(sum(3,4))

'''
o/p:
7

'''

# lets try lambda with map 

list1 = [(1,3),(2,3),(3,3),(4,3)]
sum_list = list(map(lambda  tuple1: tuple1[0]+tuple1[1],list1))
print(sum_list)

'''
o/p:
[4, 5, 6, 7]
'''
