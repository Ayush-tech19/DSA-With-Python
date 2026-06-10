def func(numbers, target):
    hash_map = {}
    for i in range(0,len(numbers)):
        looking_for = target-numbers[i]
        if looking_for in hash_map:
            return [hash_map[looking_for] , i+1]
               
        else:
            hash_map[numbers[i]]= i+1
