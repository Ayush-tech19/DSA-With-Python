# def sliding_window(arr):
#     n = len(arr)
#     max_sum = float('-inf')
#     for size in range(1 ,n+1):
#         for start in range(n-size+1):
#             window_sum = sum(arr[start:start+size])
#             max_sum = max(max_sum, window_sum)
#     return max_sum


# arr = [1,2,3,4,-5]
# print(sliding_window(arr))

def func(arr):
    max_sum = 0
    total =0
    for i in range(0 , len(arr)):
        total += arr[i]
        max_sum = max(max_sum,total)
