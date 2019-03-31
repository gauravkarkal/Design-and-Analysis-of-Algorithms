graph={'A':['B','S'],'B':['A'],'C':['S','E','D','F'],'D':['C'],'E':['C','H'],'F':['C','G'],'G':['S','F','H'],'H':['G','E'],'S':['C','G','A']}

visited=['S']
array=['S']
last='S'
level=0
while array:
    u=array.pop(0)
    print(u,level)
    for v in graph[u]:
        if v not in visited:
            w=v
            array.append(v)
            visited.append(v)
    if w in graph[last]:
        level+=1
        last=w
