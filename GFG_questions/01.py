# find the length of loop in linked list
'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''

class Solution:
    def lengthOfLoop(self, head):
        #code here
        # brute force
        travel = 0
        hash_map ={}
        temp = head
        while(temp is not None):
            if temp in hash_map:
                return travel-hash_map[temp]
            hash_map[temp] = travel
            travel +=1
            temp = temp.next
        return 0
    

# optmial solution
# using floyd's cycle detection algorithm   


class Solution:
    def lengthOfLoop(self, head):
        #code here
        s = head
        f = head
        while(f is not None and f.next is not None):
            f = f.next.next
            s = s.next
            if s==f:
                count =1
                s = s.next
                while(s != f):
                    s = s.next
                    count+=1
                return count
        return 0