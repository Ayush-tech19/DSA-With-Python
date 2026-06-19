def leaders(arr):
    result = []
    n = len(arr)
    
    for i in range(n):
      
        for j in range(i + 1, n):
          
            # If a larger element is found
            if arr[i] < arr[j]:
                break
        else:
            # If no larger element was found
            result.append(arr[i])
    
    return result


arr = [16, 17, 4, 3, 5, 2]
print(leaders(arr))