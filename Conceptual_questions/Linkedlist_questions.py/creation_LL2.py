class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class SSL:
    def __init__(self):
        self.head = None
    def append(self , val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
    def traversal(self):
        if self.head is None:
            print("LL is empty")
        else:
            curr = self.head
            while curr is not None:
                print(curr.val , end=" ->")
                curr = curr.next
            print("None")
    def insert(self,val , position):
        new_node = Node(val)
        if position==0:
            new_node.next = self.head
            self.head = new_node
        else:
            curr = self.head
            pre_node = None
            count = 0
            while curr is not None and count <position:
                pre_node = curr
                curr  = curr.next
                count+=1
            pre_node.next = new_node
            new_node.next = curr
    def delete(self , val):
        temp = self.head

        if temp.next is not None:
            if temp.val == val:
                self.head = temp.next
                return
        else:
            found = False
            prev = None
            while temp is not None:
                if temp.val == val:
                    found  = True
                    break
                prev = temp
                temp = temp.next

            if found:
                prev.next = temp.next
                del temp 
                return
            else:
                print("node not found")




        
sll = SSL()
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.append(50)
sll.traversal()
sll.insert(90,2)
sll.delete(90)
sll.traversal()


        