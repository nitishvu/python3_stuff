'''
python 3 String interpolations

1. F strings
2. str.format()
3. % formatting
4. Template strings
5. i Strings (coming soon)

'''

# 1. f strings

a = 'my'
b = 'python'

print(f'this is {a}_{b} repo.')

'''
O/P:
this is my_python repo.
'''


#we can include python expression inside strings

i= 10
j= 5
print(f'10*5 = {i*j}')

'''
O/P:
10*5 = 50
'''

#2. Str.format

print("this is {}_{} repo.".format(a,b))
'''
O/P:
this is my_python repo.
'''

#3. % formatting

print("this is %s_%s repo."%(a,b))
'''
O/P:
this is my_python repo.
'''
