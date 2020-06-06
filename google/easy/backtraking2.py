'''
nums = [3,2,5,8] k=3

'''
nums = [3,2,5,8]

def track(nums,partial,visited,result):

    if len(partial) ==3:
        result.append(partial)
        return
    for i in range(len(nums)):
        if not visited[i]:
            partial.add(nums[i])
            visited[i] = True
            track(nums,partial,visited,result)
            visited[i] = False
            partial = partial[:-1]
    return result

result = []
partial = set()
visited = [False] * len(nums)
result = track(nums,partial,visited,result)
print(result)
