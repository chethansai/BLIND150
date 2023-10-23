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

def ltl(list1):
   l1 = LinkedList()
   for i in list1:
      l1.append(i)
   return l1

def ksort(list1, list2):
   # l1 = LinkedList()
   # l2 = LinkedList()
   # for i in list1:
   #    l1.append(i)
   #
   # for i in list2:
   #    l2.append(i)
   l1 = list1
   l2 = list2

   n1 = l1.head
   n2 = l2.head
   lr = LinkedList()
   while (n1 and n2):
      if (n1.data < n2.data):
         lr.append(n1.data)
         n1 = n1.next
      else:
         lr.append(n2.data)
         n2 = n2.next

   while (n1):
      lr.append(n1.data)
      n1 = n1.next
   while (n2):
      lr.append(n2.data)
      n2 = n2.next
   return lr
#
# list1 = [1,2,4]
# list2 = [1,3,6]
# list3 =[5,7,8]
#
#
# lr = ksort(ltl(list1),ltl(list2))
# lr = ksort(lr,ltl(list3))
# lr.display()


lists = [[1,4,5],[1,3,4],[2,6]]

lr = LinkedList()
for i in lists:
   lr = ksort(lr, ltl(i))
   print(i)
   lr.display()







