class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i =0
        j =0
        m= len(word)
        n = len(abbr)
        while(i<m and j<n):
            if word[i]==abbr[j]:
                i+=1
                j+=1
            elif abbr[j].isdigit():
                if abbr[j]=="0":
                    return False
                num = 0
                while(abbr[j].isnumeric() and j<n):
                    num = num*10+ int(abbr[j])
                    j+=1
                i += num
            else:
                return False
        return i==m and j==n

