'''
print all file in a directory recursively
'''

from os import path,listdir,walk

'''
method one using list dir
'''

dir1="/home/nitish/workspace/python3_stuff"

def print_all_files(dir1,full_path):
    #print(dir1)

    if path.isdir(dir1):
        print("dir:%s"%dir1)
        files_list = listdir(dir1)
        for i in files_list:
            if '.git' in i:
                continue
            if path.isfile(full_path+'/'+i):
                print("file:%s"%(full_path+'/'+dir1+'/'+i))
            else:
                print_all_files(full_path+'/'+i,full_path+'/'+i)

print(dir1)
print_all_files(dir1,dir1)
#print(walk(dir1))
print('*'*50)
print("Now walk")
print('*'*50)

'''
method 2 using walk
'''

for root,d_names,f_names in walk(dir1):
	#print (root, d_names, f_names)
    if not('.git' in root): 
        print(root)
    for i in f_names:
        if '.git' in i or ('.git' in root): 
            continue
        print(root+"/"+i)
