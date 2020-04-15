'''
Backtraking

Systematically searches for a solution to a problem among all available options.
in bracktrking we start with one possible option out of many available options and try to solve the problem
if we are able to solve the problem  with the selected move we will print the solution else 
we will backtrak and select some other option and try to solve it.

example problem:

climbing stairs either 1 step or 2 steps number ways we can reach the last steps
lets consider 4 steps we can reach 5 ways

1+1+1+1
1+1+2
1+2+2
2+1+1
2+2

Note: i have used more variable  to explain the code flow
we can simply solve this with  climb_stairs(i+1,n)+climb_stairs(i+2,n)

'''
def climb_stairs(i,n,rec):
    print ("i=%s,n=%s,rec=%s"%(i,n,rec))
    if i== n:
        return 1
    if i> n:
        return 0
    
    return climb_stairs(i+1,n,"1")+climb_stairs(i+2,n,"2")

print(climb_stairs(0,4,"0"))


'''

O/P
i=0,n=4,rec=0
i=1,n=4,rec=1
i=2,n=4,rec=1
i=3,n=4,rec=1
i=4,n=4,rec=1
i=5,n=4,rec=2
i=4,n=4,rec=2
i=3,n=4,rec=2
i=4,n=4,rec=1
i=5,n=4,rec=2
i=2,n=4,rec=2
i=3,n=4,rec=1
i=4,n=4,rec=1
i=5,n=4,rec=2
i=4,n=4,rec=2
5

'''