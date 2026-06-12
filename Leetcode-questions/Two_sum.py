# def twoSum(nums ,target):
#         seen = {}
#         for i in range(len(nums)):
#             diff = target - nums[i]

#             if diff in seen:
#                 return[seen[diff], i]

#             seen[nums[i]] = i
        

def func(arr ,target):
    hash_map = {}
    for i in range(0,len(arr)):
        looking_for = target-arr[i]
        if looking_for in hash_map:
            return i , hash_map[looking_for]
        else:
            hash_map[arr[i]] = i






















arr= [3,2,4] 
target = 6
print(func(arr ,target))