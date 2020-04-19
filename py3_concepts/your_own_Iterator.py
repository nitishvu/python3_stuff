'''
how to create your own iter/Range function.

iterator.__iter__()
Return the iterator object itself. This is required to allow both containers and iterators 
to be used with the for and in statements. This method corresponds to the tp_iter slot of the 
type structure for Python objects in the Python/C API.

iterator.__next__()
Return the next item from the container. If there are no further items,raise the StopIteration exception.
 This method corresponds to the tp_iternext slot of the type structure for Python objects in the Python/C API.

lets try to create our own range function with return x2(x*x) of the each element x

'''

class myRange():
    def __init__(self,range):
        self.range = range
    
    def __iter__(self):
        self.x = 0
        return self
    
    def __next__(self):
        x= self.x

        if x >self.range:
            raise StopIteration
        self.x = x+1
        return x*x
    
for i in myRange(10):
    print(i)

'''
O/P:
0
1
4
9
16
25
36
49
64
81
100
'''
