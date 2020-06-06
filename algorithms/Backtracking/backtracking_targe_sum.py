nums = [10,1,2,7,6,1,1,5]
nums = sorted(nums)
print(nums)
target = 8

def getcombination(nums,target,partial,sum,start):
    if sum == target:
        print(partial)
    for i in range(start,len(nums)):
        c = nums[i]
        if (sum +c > target) or  ((i > start ) and c == nums[i-1]):
            continue
        partial.append(c)
        getcombination(nums,target,partial,sum+c,i+1)
        partial.pop()
partial = []
sum = 0
start = 0
getcombination(nums,target,partial,sum,start)
