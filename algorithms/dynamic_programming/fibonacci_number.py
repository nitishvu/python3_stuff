'''
Time to caluclate  30 th fibonacci is :0.00010800361633300781
832040

Time to caluclate  30 th fibonacci is bottom to top approach :2.193450927734375e-05
832040

Time to caluclate without cache 30 th fibonacci is :6.9141387939453125e-06
'''


import time
N=30

result_cache = {}

def get_feb(N):

    if N in result_cache:
        return result_cache[N] 
    if N==0:
        return 0
    if N==1:
        return 1
    
    
    result =  get_feb(N-1) +get_feb(N-2)
    result_cache[N] = result
    return result

'''
bottom to top approach
'''
result_cache_btop = {}
def get_feb_btop(N):
    if N==0:
        return 0
    if N==1:
        return 1
    result_cache_btop = [0] *(N+1)
    result_cache_btop[1] = 1
    for i in range(2,N+1):
        result_cache_btop[i] = result_cache_btop[i-1] +result_cache_btop[i-2]
    return result_cache_btop[N]

def get_feb_without_cache(N):

    if N==0:
        return 0
    if N==1:
        return 1
    
    
    return get_feb(N-1) +get_feb(N-2)

start_time = time.time()
print(get_feb(N))
end_time = time.time()
print("\nTime to caluclate  %s th fibonacci is :%s"%(N,(end_time-start_time)))
start_time = time.time()
print(get_feb_btop(N))
end_time = time.time()
print("\nTime to caluclate  %s th fibonacci is bottom to top approach :%s"%(N,(end_time-start_time)))
start_time = time.time()
print(get_feb_without_cache(N))
end_time = time.time()
print("\nTime to caluclate without cache %s th fibonacci is :%s"%(N,(end_time-start_time)))

'''
bottom to top approach
'''


