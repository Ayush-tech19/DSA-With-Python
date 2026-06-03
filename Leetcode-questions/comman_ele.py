def commonElements(a, b, c):
    
    # Hash Map
    count = {}

    # Process arr1 (store only unique elements)
    for i in range(len(a)):
        if i == 0 or a[i] != a[i - 1]:
            count[a[i]] = 1

    # Process arr2
    for i in range(len(b)):
        if i == 0 or b[i] != b[i - 1]:
            if count.get(b[i], 0) == 1:
                count[b[i]] = 2

    # Process arr3
    for i in range(len(c)):
        if i == 0 or c[i] != c[i - 1]:
            if count.get(c[i], 0) == 2:
                count[c[i]] = 3

    # Collect common elements
    common = []
    for key, value in count.items():
        if value == 3:
            common.append(key)

    # Sort result
    common.sort()

    return common

# dry run
# we have three arrays a, b, c
# we create a hash map to count the occurrences of elements in these arrays 
# we process arr1 and store only unique elements in the hash map with a count of 1
# we process arr2 and if an element is found in the hash map with a count of

# 1, we update its count to 2
# we process arr3 and if an element is found in the hash map with a count of
