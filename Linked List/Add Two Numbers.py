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

def addition(  ll1, ll2):
   ll3 = LinkedList()

   n1 = ll1.head
   n2 = ll2.head
   carry = 0
   while (n1 and n2):
      s1 = n1.data
      s2 = n2.data
      add = s1 + s2 + carry
      carry = add // 10
      digit = add % 10
      ll3.append(digit)
      print()
      n1 = n1.next
      n2 = n2.next

   ll3.display()



ll1 = LinkedList()
ll2 = LinkedList()

l1 = [2, 4, 3]
l2 = [5, 6, 4]
s1 = 0
s2 = 0




for i in l1:
   ll1.append(i)

for i in l2:
   ll2.append(i)



#
# ll1.display()
# ll2.display()

addition(ll1, ll2)
