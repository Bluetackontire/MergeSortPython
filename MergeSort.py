def MergeSort(A , low, high):
    if low < high :
        mid = low + (high - low) // 2 
        MergeSort(A, low, mid)
        MergeSort(A, mid + 1, high)
        Merge(A, low, mid, high)

def Merge(A , low, mid, high):
    #Calculate sizes of subarrays
    n1 = mid - low + 1
    n2 = high - mid
    
    Larray = [0] * n1
    Rarray = [0] * n2

    #Create temporary arrays to hold data
    for i in range(0, n1):
        Larray[i] = A[low + i]
    for j in range (0, n2):
        Rarray[j] = A[mid + j]
        

    #Merge Two subarrays back into original array
    i = 0
    j = 0
    k = 1

    while (i < n1) and (j < n2):
        if Larray[i] <= Rarray[j]:
            A[k] = Larray[i]
            i = i + 1 
        else:
            A[k] = Rarray[j]
            j = j + 1
        k = k + 1

    #Copy remaining elements in Larray
    while i < (n1):
        A[k] = Larray[i]
        i = i + 1
        k = k + 1
    
    #Copy elements of Rarray
    while j < n2:
        A[k] = Rarray[j]
        j = j + 1
        k = k + 1

Arr = [8, 13, 6, 20, 11, 2, 7, 16]
Larray = []
Rarray = []
S = len(Arr)
MergeSort(Arr, 0, S)
for i in range (len(Arr)):
    print(Arr[i], " ")
