def sortedSquares(nums):
        i = 0 
        j = len(nums)-1
        arr = [0]*len(nums)
        while(i<=j):
            arr[i] = nums[i]*nums[i]
            i+=1
            arr[j] = nums[j]*nums[j]
            j-=1
        arr.sort()
        return arr   #O(nlogn) TC

def sortedSquares(nums):
    if len(nums) ==0:
        return nums
    new = [0]*len(nums)
    i = 0
    j = len(nums)-1
    k = len(new)-1
    while(i<=j):
        if abs(nums[i]) > abs(nums[j]):
            new[k] = nums[i]*nums[i]
            i+=1
        else:
            new[k] = nums[j]*nums[j]
            j-=1
            k-=1
    return new