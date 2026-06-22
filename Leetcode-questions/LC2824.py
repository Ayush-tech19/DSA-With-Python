class Solution:
    def countPairs(nums, target):
        nums.sort()
        count=0
        i =0
        j=len(nums)-1
        while(i<j):
            if nums[i]+nums[j] < target:
                count+=j-i
                i+=1
            else:
                j-=1
        return count