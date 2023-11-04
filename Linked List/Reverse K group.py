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
def a(ll,k):
   d = Node(0)
   d.next = ll.head
   s = ll.head
   pg = d



   while True:
      c = getk(s,k)
      if not c:
         break
      print('c is'+ str(c.data))

      tc = c
      # current = c
      # te = c.next
      #
      # prev = None
      start = s
      s.next = c
      while(s != c):
         print('s.data' + str(s.data))
         t = s.next
         # s.next = prev
         # prev = s
         s = t

      print('outside',str(s.data))
      start.next = s
      # s.next = pg
      # pg = s
      # print("ds")
      # print("sd",s.data)




def getk(s,k):

   while s and k > 0:
      print(k, "-", s.data)
      s= s.next
      k = k - 1
   if(s):
      print('k','out-',s.data)
   return s

l =[1,2,3,4,5,6,7,8]
k = 3
ll = LinkedList()
for i in l:
   ll.append(i)

ll.display()




a(ll,k)
print('okay')
ll.display()






