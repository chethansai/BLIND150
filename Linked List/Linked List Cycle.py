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
   def chain(self):
      self.tail.next = self.head
   # def sol(self, pos):
   #    start = self.head
   #
   #    while(pos):
   #       pos = pos - 1
   #       print(pos)
   #       start = start.next
   #       print(start.data)
   #    start1 = start
   #
   #    while(start1):
   #       print("o")
   #       print(start.data)
   #       print(start1.data)
   #       print(start1.next.data)
   #       if(start1.next == start):
   #          print("equals")
   #          print(start1.next.next.data)
   #          break
   #
   #       start1 = start1.next
   def sol(self,pos):
      h =set()
      n = self.head
      while(n):
         if n not in h:
            h.add(n)

         else:
            print('False')
            return False
         n = n.next
      print('True')




head = [3,2,0,-4]
pos = 1
ll = LinkedList()
for i in head:

   ll.append(i)
ll.chain()
#
# ll.display()
ll.sol(pos)








