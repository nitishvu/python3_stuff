'''
If we define the function F(n) to represent the Fibonacci number at the index of n, 
then you can derive the following recurrence relation:

F(n) = F(n - 1) + F(n - 2)
with the base cases:

F(0) = 0, F(1) = 1

Now, if you would like to know the number of F(4), you can apply and extend the above formulas as follows:

F(4) = F(3) + F(2) = (F(2) + F(1)) + F(2)

# Memoization
To eliminate the duplicate calculation in the above case, as many of you would have figured out,
one of the ideas would be to store the intermediate results in the cache
so that we could reuse them later without re-calculation.

This idea is also known as memoization, which is a technique that is frequently used together with recursion.
'''

def fib(n):
    fib_cache = {}

    def fib_recursion(n):
        # print n to understand the recursion flow
        #print(n)
        if n in fib_cache:
            return fib_cache[n]

        if n <2 :
            result = n
        else:
            result = fib_recursion(n-1) + fib_recursion(n-2)

        fib_cache[n] = result
        return result

    return fib_recursion(n)

print(fib(5))
