strings = ["acd", "dfg", "wyz", "yab", "mop","bdfh", "a", "x", "moqs"]

group_dict = {}

for string in strings:
    cur_len = len(string)
    if cur_len in group_dict:
        group_dict[cur_len] += [string]
    else:
        group_dict[cur_len] = [string]

print (group_dict)