# using extra space
def func(numbers, target):
    hash_map = {}
    for i in range(0,len(numbers)):
        looking_for = target-numbers[i]
        if looking_for in hash_map:
            return [hash_map[looking_for] , i+1]
               
        else:
            hash_map[numbers[i]]= i+1


# without using extra space
# so we are given that array is soretd
def twoSum(numbers ,target):
    i = 0
    j = len(numbers)-1
    while(i<j):
        if numbers[i]+numbers[j] > target:
            j-=1
        elif numbers[i]+numbers[j]  < target:
            i+=1
        else:
            return [i+1 ,j+1]
