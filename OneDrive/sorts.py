import random
randomlist = random.sample(range(0, 1000000), 100000)

f = open("bignum.txt", "w")
for i in randomlist:
    f.write(str(i)+"\n")

f.close
f = open("bignum.txt", "r")


arr = [f for f in f.readlines()]
f.close

def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
    return arr

def timer(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("Time taken by {} is {}".format(func.__name__, end-start))
    return wrapper

timer(bubbleSort)(arr)
#timer(insertionSort)(arr)
#timer(mergeSort)(arr)
#timer(quickSort)(arr, 0, len(arr)-1)
# sorted = quickSort(arr, 0, len(arr)-1)



def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr



def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1
        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1
        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1
    return arr


def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
    return arr

def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] < pivot:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


def timer(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("Time taken by {} is {}".format(func.__name__, end-start))
    return wrapper

#timer(bubbleSort)(arr)
#timer(insertionSort)(arr)
#timer(mergeSort)(arr)
#timer(quickSort)(arr, 0, len(arr)-1)
# sorted = quickSort(arr, 0, len(arr)-1)

# f = open("/home/graham/Code/bignum.txt", "w")
# for i in sorted:
#     f.write(str(i)+"\n")
# f.close()



    


