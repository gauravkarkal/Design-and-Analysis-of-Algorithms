import random
import time
def partition(low,high):
    b=low-1
    pivot=array[high]

    for j in range(low,high):
        if array[j]<=pivot:
            b=b+1
            array[b],array[j]=array[j],array[b]
    array[b+1],array[high]=array[high],array[b+1]
    return b+1

def quicksort(low,high):
    if low<high:
        pi=partition(low,high)
        quicksort(low,pi-1)
        quicksort(pi+1,high)

array=random.sample(range(100),10)
start=time.clock()
quicksort(0,len(array)-1)
end=time.clock()
print("time=",end-start)5
print(array)
    
