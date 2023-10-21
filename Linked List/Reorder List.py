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
   def display(self):
      c = self.head
      while(c):
         print(c.data)
         c = c.next

   def invert(self):

      slow, fast = self.head,self.head.next
      while(fast):
         slow = slow.next
         fast = fast.next.next



      #reverse
      second = slow.next
      slow.next = None
      prev = None

      while(second):
         t = second.next
         second.next = prev
         prev = second
         second =t


      first, second = self.head, self.tail
      while(second):
         t1, t2 = first.next, second.next
         first.next = second

         second.next  = t1
         first, second = t1, t2





ll = LinkedList()
h = [1,2,3,4,5]
for i in h:
   ll.append(i)

ll.display()
ll.invert()
ll.display()
ha = [1,5,2,4,3]








