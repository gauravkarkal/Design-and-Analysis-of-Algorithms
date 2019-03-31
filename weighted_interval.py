n=6
jobs=[[99,0,99],[1,2,100],[2,5,200],[3,6,300],[4,8,400],[5,9,500],[6,10,100]]

start=0
finish=1
value=2


jobs.sort(key=lambda x:x[1])

P=[0]*(n+1)
M=[0]*(n+1)

def pj(n):
    for i in range(n,1,-1):
        for j in range(i-1,0,-1):
            if jobs[i][start]>=jobs[j][finish]:
                P[i]=j
                break

def OPT(n):
    for j in range(1,n+1):
        M[j]=max(jobs[j][value]+M[P[j]],M[j-1])

def find(n):
    if n>0:
        if jobs[n][value]+M[P[n]]>=M[n-1]:
            print(n)
            find(P[n])
        else:
            find(n-1)

pj(n)
OPT(n)
find(n)
print(M[n])
