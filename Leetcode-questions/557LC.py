# word = "thr ske is bleu"
# s = word.split()

# s.reverse()
# print(s)  #just for recalling some concepts

def func(s):
    left  = 0
    n = len(s)
    while left<n and s[left]==" ":
        left+=1
        continue
    right = n-1
    while right>=0 and s[right] == " ":
        right-=1
        continue
    sttr = ""
    word = []
    while(right>=left):
        if s[right]!= " ":
            sttr+=s[right]
            right-=1
        else:
            if sttr:
                word.append(sttr)
                sttr = ""
                right-=1
    if sttr:
        word.append(sttr)
    word.reverse()
    return " ".join(word)

s = "the sky is"
print(func(s))

        

        