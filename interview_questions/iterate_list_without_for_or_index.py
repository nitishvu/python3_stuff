'''
lets try to iterrate a list elments wihtout using for loop or index

iter :create a iterable object
next; returns  next elelment in the iterable obj and raise StopIteration exception if elments are returned.
'''

list1 = [1,2,4,5,6]

iter_obj = iter(list1)

while True:
    try:
        item = next(iter_obj)
        print(item)
    except StopIteration:
        break
