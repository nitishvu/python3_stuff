'''Given a fence with n posts and k colors, find out the number of ways
of painting the fence such that at most 2 adjacent posts 
have the same color. Since answer can be large return it modulo 10^9 + 7.

Input : n = 2 k = 4
Output : 16
We have 4 colors and 2 posts.
Ways when both posts have same color : 4 
Ways when both posts have diff color :
4*(choices for 1st post) * 3(choices for 
2nd post) = 12

Input : n = 3 k = 2
Output : 6
'''

n=3
k=2

used = [0]*k
def paint(n,k,used,result,partial):



    if partial >= n:
        result = result +1
        return result

    for i in range(0,k):
        if not used[i] >= 2:
            used[i] +=1
            partial +=1
            result = paint(n,k,used,result,partial)
            used[i] -=1
            partial -=1

    return result
result = 0
partial = 0
result = paint(n,k,used,result,partial)   
print (result)

    