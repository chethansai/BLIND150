# class Node:
#    def __init__(self,data):
#       self.data = data
#       self.next = None
#
# class LinkedList:
#    def __init__(self):
#       self.head = None
#       self.tail = None
#
#    def append(self,data):
#       new_node = Node(data)
#
#       if( self.head is None):
#          self.head = new_node
#          self.tail = new_node
#
#       else:
#          self.tail.next= new_node
#          self.tail = new_node
#
#    def delete(self,data):
#
#       if(self.head is None):
#          return
#       if(self.head.data == data):
#          self.head = self.head.next
#          return
#       c = self.head
#       while(c.next):
#          if(c.next.data == data):
#             c.next =  c.next.next
#             return
#          c =c.next
#    def display(self):
#       c = self.head
#       while(c):
#          print(c.data)
#          c = c.next
# def a(ll,k):
#    d = Node(0)
#    d.next = ll.head
#    s = ll.head
#    pg = d
#
#
#
#    while True:
#       c = getk(s,k)
#       if not c.next:
#          break
#       # current = c
#       # te = c.next
#       #
#       # prev = None
#       while(s and s != c):
#          print('s.data' + str(s.data))
#          t = s.next
#          # s.next = prev
#          # prev = s
#          s = t
#
#       print('outside',str(s.data))
#       # s.next = pg
#       # pg = s
#       # print("ds")
#       # print("sd",s.data)
#
#
#
#
# def getk(s,k):
#
#    while s and k > 0:
#       print(k, "-", s.data)
#       s= s.next
#       k = k - 1
#
#    print('k','out-',s.data)
#    return s
#
# l =[1,2,3,4,5,6,7,8]
# k = 3
# ll = LinkedList()
# for i in l:
#    ll.append(i)
#
# ll.display()
#
#
#
#
# a(ll,k)
# print('okay')
# ll.display()
#
#
#
#
#
#


class Node:
   def __init__(self, data):
      self.left = None
      self.data = data
      self.right = None

class Bst:
   def __init__(self):
      self.root = None

   def insert(self, data):
      if self.root is None:
         self.root = Node(data)
      else:
         self.insert_recursively(self.root, data)
   def insert_recursively(self, current, data):
      if(current.data<data):
         if (current.right is None):
            current.right = Node(data)
         else:
            self.insert_recursively(current.right, data)
      else:
         if (current.left is None):
            current.left = Node(data)
         else:
            self.insert_recursively(current.left, data)

   def inorder(self,current):
      if (current.left):
         self.inorder(current.left)
      if(current.data):
         print(current.data)
      if (current.right):
         self.inorder(current.right)


t = Bst()
t.insert(1)
t.insert(2)
t.insert(3)
t.insert(4)

t.inorder(t.root)

