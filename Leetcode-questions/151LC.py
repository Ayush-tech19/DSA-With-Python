
# lst = s.split()
# print(lst)

# def func(s):
#     v = ""
#     lst = s.split()
#     for i in range(len(lst)-1 , -1,-1):
#         v += lst[i] + " "
#     return v
# print(func("   The  sky is blue   " ))

def func(s):
    chars = []
    left = 0
    while(left<len(s) and s[left]==" "):
        left+=1
    right = len(s)-1
    while(right>=0 and s[right]==" "):
        right-=1
    sttr = ""
    while(left<=right):
        if s[left] != " ":
            sttr+= s[left]
            # left+=1
        else:
            if sttr:
              chars.append(sttr)
              sttr = ""
        left+=1

    if sttr:
        chars.append(sttr)
    
    i =0
    j = len(chars)-1
    while(i<j):
        chars[i] , chars[j] = chars[j] , chars[i]
        i+=1
        j-=1

            
    return " ".join(chars)

print(func("  The sky    is blue"))


