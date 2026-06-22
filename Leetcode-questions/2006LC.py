def countKDifference(nums, k):
    hash_map = {}
    count = 0
    for i in range(0, len(nums)):
        if nums[i] in hash_map:
            hash_map[nums[i]] += 1
        else:
            hash_map[nums[i]] =1
        for i in range(0 ,len(nums)):
            if nums[i]-k in hash_map:
                count += hash_map[nums[i]-k]

    return count