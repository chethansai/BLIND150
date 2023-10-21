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
   def display1(self,a):
      c = a
      while(c):
         print(c.data)
         c = c.next

   def ran(self):

      c = self.head
      d= dict()
      while(c):
         d[c] = Node(c.data)
         c = c.next
      c = self.head
      while(c):
         if(c.next):
            d[c].next = d[c.next]
         c = c.next
      return d[self.head]


h=[7,13,11,10,1]
ll = LinkedList()
for i in h:
   ll.append(i)
ll.display()


ll.display1(ll.ran())





