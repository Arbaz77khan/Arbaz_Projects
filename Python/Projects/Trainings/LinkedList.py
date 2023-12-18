
class Node:
    
    def __init__(self, value):
        self.data = value
        self.next = None

class Linkedlist:
    
    def __init__(self):
        # Empty Linked list
        self.head = None

        # No. of nodes in LL
        self.n = 0  

    def __len__(self):
        return self.n
    
    def insert_head(self, value):

        # create a new node
        new_node = Node(value)

        # create a connection
        new_node.next = self.head

        # Assigning head
        self.head = new_node

        # increment n
        self.n = self.n + 1

    def __str__(self):

        curr = self.head

        result = "["
        while curr != None:
            # print(curr.data)
            result = result + str(curr.data) + ", "
            curr = curr.next
        result = result[:-2] + "]"

        return result
    
    def append(self, value):

        # create a new node
        new_node = Node(value)

        curr = self.head

        if (curr == None):
            self.head = new_node
        else:
            # traverse LL to last node
            while curr.next != None:
                curr = curr.next
            curr.next = new_node
        
        # increment n
        self.n = self.n + 1


L = Linkedlist()
L.insert_head(1)
L.insert_head(2)
L.insert_head(3)
L.insert_head(4)
print(len(L))
L.append(5)
print(len(L))
print(L)
