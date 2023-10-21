class Node:
   def __init__(self,data):
      self.data = data
      self.next = None

class LinkedList:
   def __init__(self):
      self.head = None
      self.tail = None

   def append(self,data):
      new_node = Node(data)

      if( self.head is None):
         self.head = new_node
         self.tail = new_node

      else:
         self.tail.next= new_node
         self.tail = new_node

   def delete(self,data):

      if(self.head is None):
         return
      if(self.head.data == data):
         self.head = self.head.next
         return
      c = self.head
      while(c.next):
         if(c.next.data == data):
            c.next =  c.next.next
            return
         c =c.next

   def rem(self,n):
      dummy = Node(0)
      dummy.next = self.head
      left = dummy
      right = self.head

      while(n):
         right = right.next
         n = n - 1
      while(right):
         right = right.next
         left = left.next

      left.next = left.next.next
      return dummy.next


   def display(self):
      c = self.head
      while(c):
         print(c.data)
         c = c.next

ll = LinkedList()
head = [1,2,3,4,5]
n = 2

for i in head :
   ll.append(i)

ll.display()

ll.rem(n)
ll.display()





