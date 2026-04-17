def containsDuplicate(nums):
    hash_map = {}
    for i in range(0 , len(nums)):
        if nums[i] in hash_map:
            hash_map[nums[i]] += 1
        else:
            hash_map[nums[i]] = 1
    for k , v in hash_map.items():
        if v>1:
            return True
        
    return False
arr = [2,14,18,22,22]
print(containsDuplicate(arr))