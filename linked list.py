# making a linked list manually.

# class Node:
#     def __init__(self,value):
#         self.data = value
#         self.next = None

# a = Node(1)
# b=Node(2)
# c=Node(3)
# a.next=b
# b.next=c

# print(a.next)
##############----------------------################---------#####
class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class LinkedList:
        def __init__ (self):
            # create a empty linked list
            self.head = None
            #number of nodes in LL
            self.n = 0
    
        def __len__(self):
            return self.n
        
        def insert_head(self,value):
            #new node
            new_node = Node(value)

            #create connection 
            new_node.next =  self.head

            #reassign head
            self.head = new_node

            #increment n
            self.n += 1

        def __str__(self):
            curr = self.head
            result = ''
            while curr != None :
                result = result+ str(curr.data) + '->'
                curr = curr.next
            return result[:-2]
        
        def append(self,value):
            new_node = Node(value)
            if self.head== None: 
                #empty
                self.head = new_node
                self.n += 1
                return
            curr = self.head
            while curr.next != None:
                curr = curr.next
            # you are at the last node
            curr.next = new_node
            self.n += 1
        
        def insert_after(self,after,value):
            new_node = Node(value)
            curr = self.head
            while curr != None:
                if curr.data == after:
                    break
                curr = curr.next
            # case 1 break - item has been found
            if curr != None:
                new_node.next = curr.next
                curr.next = new_node
                self.n = self.n +1 
            else:
                return "Item not found"
            # case 2 loop worked full -> item not found -> curr -> None

        def clear(self):
            self.head = None
            self.n = 0 
        def delete_head(self):
            if self.head == None:
                return "empty LL"
            
            self.head = self.head.next
            self.n -= 1

        def pop(self):
            if self.head == None:
                return " Empty Linked List"
            curr = self.head
            # check if LL has only one node
            if curr.next == None:
                return self.delete_head()
            while curr.next.next != None:
                curr= curr.next
            # curr => 2nd last node
            curr.next =  None
            self.n -= 1
        
        def remove (self,value):
            if self.head == None:
                return "Empty Linked list"
            if self.head.data == value:
                # you want to remove head node
                return self.delete_head()
            curr = self.head
            while curr.next != None:
                if curr.next.data == value:
                    break
                curr = curr.next
            
            # 2 cases item found
            # item not found
            if curr.next == None:
                return "not found"
            else:
                curr.next = curr.next.next 
        
        def search (self,item):
            curr = self.head
            pos = 0
            while curr != None:
                if curr.data == item:
                    return pos
                curr = curr.next
                pos = pos + 1
            return "Not Found"

        def __getitem__(self,index):
            curr = self.head
            pos = 0

            while curr !=None:
                if pos == index:
                    return curr.data
                curr = curr.next
                pos = pos +1
L = LinkedList()
L.insert_head(1)
L.insert_head(2)
L.insert_head(3)
L.insert_head(4)
L.insert_head(5)
print(L)
print(L[2])



# L2 = LinkedList()
# L2.append(5)
# print(L2)
# L2.insert_after(5,100)
# print(L2)
 
# L3 = LinkedList()
# print(L3.insert_after(5,100))