
input1 = [1,2,3]
partial = []
used = [False] *len(input1)
print(used)

print(input1[::-1])
def track(input1,partial,used,result):

    if len(input1) == len(partial):
        print(partial)
        result.append([partial])
        #print(result)
        return

    for i in range(0,len(input1)):
        if not used[i]:
            used[i] = True
            partial = partial + [input1[i]]
            track(input1,partial,used,result)
            #print(partial,i)
            used[i] = False
            partial = partial[:-1]

    
result=[]
track(input1,partial,used,result)
print(result)
print(len(result))
