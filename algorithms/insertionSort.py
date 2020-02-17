def insertionSort(arr): 
    for i in range(1, len(arr)):
        vindex = i
        lindex = i - 1
        
        while lindex >= 0 and arr[lindex] > arr[vindex]:
            arr[lindex], arr[vindex] = arr[vindex], arr[lindex]
            vindex -= 1
            lindex -= 1

    return arr


  
arr = [31, 41, 59, 26, 41, 58, 6] 
insertionSort(arr) 
for i in range(len(arr)): 
    print ("% d" % arr[i]) 
  