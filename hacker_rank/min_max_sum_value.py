def miniMaxSum(arr):
    arr.sort()
    min_sum = sum(arr[0:4])
    max_sum = sum(arr[1:])
    return (min_sum, max_sum)  

arr = [1, 2, 3, 4, 5]
result = miniMaxSum(arr)
print(result)  # Output: (10, 14)


# otptimal soltution

def miniMaxSum(arr):
    total = sum(arr)
    min_sum = total - max(arr)
    max_sum = total - min(arr)
    print(min_sum , max_sum)

arr2 = [10 , 20 , 30 , 40 , 50]
result2 = miniMaxSum(arr)
print(result2) 