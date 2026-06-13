def func(s , abbr):
    i = 0
    j = 0
    while(i<len(s)):
        count = 0
        if s[i] == abbr[j]:
            i+=1
            j+=1
        elif s[i] != abbr[j]:
            if abbr[j].isdigit():
                val = int(abbr[j])
                while(i<=val):
                    i+=1
                    count+=1
                if count != i:
                    return False
        
    return True

print(func("apple", "a3e"))

                    


