input_str = "god"
part = ""
visited = [False]* len(input_str)

def track(input_str,part,visited):
    if len(part) == len(input_str):
        print(part)
        return
    
    for i in range(0,len(input_str)):
        if not visited[i]:
            visited[i] = True
            part += input_str[i]
            track(input_str,part,visited)
            visited[i] = False
            part = part[:-1]

track(input_str,part,visited)