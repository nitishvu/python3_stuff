n=3
chars = ['(']*n + [')']*n
print(chars)
result = []
partial= ""

l=0
r=0
def track(chars,partial,result,l,r):

    if len(partial) == n*2:
        result.append(partial)
        return result

    if l<n:
        partial = partial + '('
        result = track(chars,partial,result,l+1,r)
        partial = partial[:-1]
    if r<l:
        partial = partial + ')'
        result = track(chars,partial,result,l,r+1)
        partial = partial[:-1]
    return result
result = track(n,partial,result,l,r)
print(result)




