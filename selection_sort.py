import random
def selection_sort(A):
    for i in range(0,len(A)-1):
        minimum=i
        for j in range(i,len(A)):
            if A[minimum]>A[j]:
                minimum=j
        A[minimum],A[i]=A[i],A[minimum]
A=random.sample(range(100),10)
print(A)
selection_sort(A)
print(A)
