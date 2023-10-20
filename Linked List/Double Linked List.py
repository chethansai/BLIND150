class Node:
   def __init__(self, data):
      self.data = data
      self.next = None
      self.prev = None


class DoublyLinkedList:
   def __init__(self):
      self.head = None
      self.tail = None

   def append(self, data):
      new_node = Node(data)
      if self.head is None:
         self.head = new_node
         self.tail = new_node
      else:
         new_node.prev = self.tail
         self.tail.next = new_node
         self.tail = new_node

   def delete(self, data):
      current = self.head
      while current:
         if current.data == data:
            if current.prev:
               current.prev.next = current.next
            if current.next:
               current.next.prev = current.prev
            if current == self.head:
               self.head = current.next
            if current == self.tail:
               self.tail = current.prev
            return
         current = current.next

   def display(self):
      current = self.head
      while current:
         print(current.data, end=" <-> ")
         current = current.next
      print("None")
