import random
def insertion_sort(A):
    for i in range(1,len(A)):
        j=i-1
        while A[j]>A[j+1] and j>=0:
            A[j],A[j+1]=A[j+1],A[j]
            j=j-1

A=random.sample(range(100),10)
print(A)
insertion_sort(A)
print(A)
