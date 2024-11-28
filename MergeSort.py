def MergeSort(A , low, high):
    if low < high :
        mid = (low + high) // 2
        MergeSort(A, low, mid)
        MergeSort(A, mid + 1, high)
        Merge(A, low, mid, high)

def Merge(A , low, mid, high):
    #Calculate sizes of subarrays
    n1 = mid - low + 1
    n2 = high - mid

    #Create temporary arrays to hold data
    for i in range(n1):
        Larray[i] = A[low + i - 1]
    for j in range (n2):
        Rarray[j] = A[mid+j]

    #Merge Two subarrays back into original array
    i = 1
    j = 1
    k = low

    while (i <= n1) and (j <= n2):
        if Larray[i] <= Rarray[j]:
            A[k] = Larray[i]
            i = i + 1 
        else:
            A[k] = Rarray[j]
            j = j + 1
        k = k + 1

    #Copy remaining elements in Larray
    while i <= n1:
        A[k] = Larray[i]
        i = i + 1
        k = k + 1
    
    #Copy elements of Rarray
    while j <= n2:
        A[k] = Rarray[j]
        j = j + 1
        k = k + 1

S = Arr.length
MergeSort(Arr, 1, S)
for i in range(S):
    print(Arr[i])
