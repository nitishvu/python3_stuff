'''
nums = [3,2,5,8] k=3

'''
nums = [3,2,5,8]

def track(nums,partial,start,result):

    if len(partial) ==3:
        print(partial)
        temp = partial.copy()
        result.append(temp)
        return
    if start == len(nums):
        return
    for i in range(start,len(nums)):
            partial.add(nums[i])
            track(nums,partial,i+1,result)
            partial.remove(nums[i])
    return result

result = []
start = 0
partial = set()
visited = [False] * len(nums)
result = track(nums,partial,start,result)
print(result)
