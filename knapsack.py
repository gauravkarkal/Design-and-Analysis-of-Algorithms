n=4
W=7
weight=[99,3,5,6,2]
value=[99,10,4,9,11]

M=[[0]*(W+1) for x in range(n+1)]

for i in range(1,n+1):
    for w in range(1,W+1):
        if weight[i]<=w:
            M[i][w]=max(value[i]+M[i-1][w-weight[i]],M[i-1][w])
        else:
            M[i][w]=M[i-1][w]

i=n
k=W

while i>0 and k>0:
    if M[i][k]!=M[i-1][k]:
        print(i)
        k=k-weight[i]
    i=i-1
