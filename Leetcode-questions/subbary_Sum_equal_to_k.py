# def subarraySum(nums, k):
#         count = 0
#         for i in range(0 ,len(nums)):
#             total = 0
#             for j in range(i , len(nums)):
#                 total += nums[j]
#                 if total == k:
#                     count+=1
#         return count


# optimized solution using hashmap
def subarraySum(nums, k):
        count = 0
        sum_so_far = 0
        sum_freq = {0: 1}  

        for num in nums:
            sum_so_far += num
            
            if (sum_so_far - k) in sum_freq:
                count += sum_freq[sum_so_far - k]
            
            # Update the frequency of the current sum
            if sum_so_far in sum_freq:
                sum_freq[sum_so_far] += 1
                sum_freq[sum_so_far] += 1
            else:
                sum_freq[sum_so_far] = 1
        
        return count

# Example usage:
nums = [1, 1, 1]
k = 2
print(subarraySum(nums, k))  # Output: 2