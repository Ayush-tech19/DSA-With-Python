def func(arr):  #arr having 0 and 1 only
    i = 0
    j = len(arr)-1
    while(i<=j):
        if arr[i] ==0:
            i+=1
        else:
            arr[i] ,arr[j] = arr[j] ,arr[i]
            j-=1
    return arr


arr = [0,1,0,1,1,0,1]
print(func(arr))