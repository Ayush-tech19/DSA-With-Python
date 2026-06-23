def func(string):
    hash_map = {}
    hash_map.update({"1": "1", "0": "0", "8": "8" , "6": "9", "9": "6"})
    i =0
    j = len(string)-1
    while(i<=j):
        if string[i] in hash_map:
            if hash_map[string[i]] != string[j]:
                return False
            i+=1
            j-=1
        else:
            return False
    return True

print(func("198261"))

    

