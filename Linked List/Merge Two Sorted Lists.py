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

list1 = [1,2,4]
list2 = [1,3,4]

l1 = LinkedList()
l2 = LinkedList()
for i in list1:
   l1.append(i)

for i in list2:
   l2.append(i)
n1 = l1.head
n2 = l2.head
lr = LinkedList()
while(n1 and n2):
   if(n1.data<n2.data):
      lr.append(n1.data)
      n1 =n1.next
   else:
      lr.append(n2.data)
      n2 = n2.next

while(n1):
   lr.append(n1.data)
   n1 = n1.next
while(n2):
   lr.append(n2.data)
   n2 = n2.next
lr.display()








