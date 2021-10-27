# A single node of a singly linked list
class Node:
  # constructor
  def __init__(self, data): 
    self.data = data
    self.next = None

# A Linked List class with a single head node
class LinkedList:
  def __init__(self):  
    self.head = None
  
  # insertion method for the linked list
  def insert(self, data):
    new_node = Node(data)
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
      current.next = new_node
    else:
      self.head = new_node
  
  # print method for the linked list
  def print_List(self):
    current = self.head
    while(current):
      print(current.data)
      current = current.next

# Singly Linked List with insertion and print methods
L_List = LinkedList()
L_List.insert(23)
L_List.insert(43)
L_List.insert(83)
L_List.insert(83)
L_List.insert(83)
L_List.insert(100)
L_List.print_List()