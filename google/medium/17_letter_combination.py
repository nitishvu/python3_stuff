number_map = {1:"", 2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"waxyz"}
digits="23"
digits= [i for i in digits]
print(digits)
digits=[2,3]        
result = []
index = 0
partial=""

if digits=="":
    return  []
digits = [int(i) for i in digits ]
if len(digits) ==1:
    result = [i for i in number_map[digits[0]]]
    return result
def track(digits,number_map,result,partial,index):
    
    if index == len(digits):
        result.append(partial)
        return result
    
    for i in number_map[digits[index]]:

        result = track(digits,number_map,result,partial+i,index+1)
    return result
result = track(digits,number_map,result,partial,index)
print (result)