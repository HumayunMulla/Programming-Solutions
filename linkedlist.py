
# LINKED LIST
# A Linked List (LL) is a data structure that is made up of chain of node objects. 
# Each node contains a value (data) and a pointer to the next node in the chain.
# head pointer points to the first/head node of the LL and the last node's 
# next pointer is null. When the list is empty the head pointer points to null.
# Ex. 15 -> 10 -> 1 -> 5

# Create a single node
class Node:
    # contructor
   def __init__(self, data, next=None):
    self.data = data
    self.next = next

# create a single node
# first = Node(786)
# print(first.data)
        
# Join multiple nodes to create a LL
# create a head node 

# A LinkedList Class with a single head node
class LinkedList:
    # constructor
    def __init__(self):
        self.head = None

    # list manipulation methods

    # INSERTION
    def insert(self, data):
        # create a new node
        new_node = Node(data)
        # check if head exists
        if(self.head):
            # take current head into a temp node
            current_node = self.head
            # traverse to the last current element
            while(current_node.next):
                # get the last element in the existing list
                current_node = current_node.next
            # point the last element's value to new node
            current_node.next = new_node
        else:
            # since there is no head make this node as the head
            self.head = new_node
    
    # PRINTING
    def print_list(self):
        # first go to the first node
        current_node = self.head
        # until you reach the last element in the list
        # make a list for better presentation
        print_linkedlist = []
        while(current_node):
            # print the node value
            print_linkedlist.append(current_node.data)
            # now iterate and go to the next element
            current_node = current_node.next
        
        print(print_linkedlist)

        
# PROBLEM
# Given a singly linked list, find its middle element. If there are an even number of nodes, then there are two middle nodes; return the second middle element in cases like this.
# Example
# For l = [5, 4, 3, 2, 1], the output should be
# solution(l) = 3;
# For l = [10, 8, 6, 4, 2, 0], the output should be
# solution(l) = 4.

def solution(l):
    # LinkedList.print_list(l)
    
    Linked_List = []
    
    # Get the count of nodes
    current_node = l.head
    length = 0
    while(current_node is not None):
        length = length + 1
        Linked_List.append(current_node.data)
        current_node = current_node.next
        
    
    print(Linked_List[int(length/2)])
            

    



# Linked List with a single node
# LL = LinkedList()
#LL.head = Node(786)
# print(LL.head.data)

# Create a Linked List
LL = LinkedList()
# LL.insert(5)
# LL.insert(4)
# LL.insert(3)
# LL.insert(2)
# LL.insert(1)
LL.insert(10)
LL.insert(8)
LL.insert(6)
LL.insert(4)
LL.insert(2)
LL.insert(0)




# print the list
LL.print_list()

# PROBLEM SOLUTION
solution(LL)