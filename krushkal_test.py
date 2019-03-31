n=5
graph=[[1,2,4],[2,3,3],[2,4,1],[1,4,8],[4,3,7],[3,5,8],[4,5,3]]

graph.sort(key=lambda x:x[2])

parent=[-1]*(n+1)
final=[]
count=0

def get_parent(node):
    if parent[node]==-1:
        return node
    else:
        return get_parent(parent[node])

def union(a,b):
    pa=get_parent(a)
    pb=get_parent(b)
    parent[pa]=pb

def krushkal(n):
    global count
    for edge in graph:
        if count==n-1:
            break
        u=edge[0]
        v=edge[1]

        pu=get_parent(u)
        pv=get_parent(v)
        if pu!=pv:
            final.append(edge)
            union(u,v)
            count=count+1
krushkal(n)
print(final)
            
