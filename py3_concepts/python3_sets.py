'''
Python3 sets 
1.Normal set = set()

unorldered list,mutalble,no duplicates

2.Frozen sets = forzenset()
immutable,unordered


Note:
You can't put a set in a set because sets can only contain immutable (hashable) types.
You can convert your set to a tuple or a frozenset to make it immutable and qualify for being put into a set.


Note:Set items cannot be accessed by referring to an index,
since sets are unordered the items has no index.
But you can loop through the set items using a for loop
or ask if a specified value is present in a set, by using the in keyword.



3. add/update/discard/remove elments to set set.add(),set.update(),set.discard()
->update is used for adding 2 or more elements.
set1.update([1,2])
-> discard to remove a element form the set. (no error if element not present)
sets1.discard(element) 
-> remove to remove a element form the set. (Error if element not present)
sets1.remove(element) 


4.union of sets.
set3= set1.union(set2)

5. intersection of sets.
set3 = set1.intersection(set2) 

6.difference of sets.
set3 = set1.difference(set2) 

7. to empty a set
set1.clear() 

8. max(set)
finding maximum number in a set

'''



#1.Normal set = set()

normal_set = set(['a','b','c'])
print(normal_set)
normal_set.add('b')
print(normal_set)
normal_set.add('d')
print(normal_set)

'''
O/P:
{'c', 'b', 'a'}
{'c', 'b', 'a'}
{'c', 'b', 'a', 'd'}
'''

#2.Frozen sets = forzenset()
frozen_set = frozenset(['a','b','c'])

#frozen_set.add('b')
# AttributeError: 'frozenset' object has no attribute 'add'
print(frozen_set)


#8. max of set 

number_set = set([2,5,2,4,6,2,5,6])
print(max(number_set))

#O/P:6