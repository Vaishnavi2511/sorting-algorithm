"""
In this algorithm we repeatedly swap the elements until correct order is reached
Each element is compared with the adjacent element and swapped accordingly
            if arr[j] > arr[j+1] then 
            arr[j],arr[j+1] = arr[j+1],arr[j]         
"""
def algorithm(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    for k in range(n):
        print(arr[k])
arr = [83,1,45,95,45,52,11,47,0,45,67,82]
algorithm(arr)
   
