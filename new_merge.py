count=0
import random
def merge(left,right):
    i=0
    j=0
    c=[]
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            c.append(left[i])
            i=i+1
        else:
            c.append(right[j])
            global count
            count=count+(len(left)-i)
            j=j+1
    c.extend(left[i:])
    c.extend(right[j:])
    '''
    while i<len(left):
        c.append(left[i])
        i=i+1
    while j<len(right):
        c.append(right[j])
        j=j+1
    '''
    print("Merging",c)
    return c

def merge_sort(A):
    print("Splitting",A)
    if len(A)>1:
        mid=len(A)//2
        lefthalf=merge_sort(A[:mid])
        righthalf=merge_sort(A[mid:])
        A=merge(lefthalf,righthalf)
    return A

#B=random.sample(range(100),10)
#B=[6,5,4,3,2,1]
B=[2,4,1,3,5]
print(B)
D=merge_sort(B)
print(D)
print(count)
