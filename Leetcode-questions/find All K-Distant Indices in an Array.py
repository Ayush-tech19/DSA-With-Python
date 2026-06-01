def func(nums , key , k):
    res = []
    for i in range(len(nums)):
        if nums[i] == key:
            for j in range(max(0, i-k), min(len(nums), i+k+1)):
                if j != i and j not in res:
                    res.append(j)
    return res

print(func([3,4,9,1,3,9,5], key = 9, k = 1)) # [0,1,2,3,4]

