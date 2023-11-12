class Node:
   def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None


class BinarySearchTree:
   def __init__(self):
      self.root = None

   def insert(self, data):
      if self.root is None:
         self.root = Node(data)
      else:
         self.insert_recursively(data, self.root)

   def insert_recursively(self, data, current_node):
      if current_node.data > data:
         if current_node.left is None:
            current_node.left = Node(data)
         else:
            self.insert_recursively(data, current_node.left)
      else:
         if current_node.right is None:
            current_node.right = Node(data)
         else:
            self.insert_recursively(data, current_node.right)

   def inorderrdfs(self, CNode,k):
      if not CNode:
         return

      if CNode.left:
         self.inorderrdfs(CNode.left,k)





      if (k == 1):
         print( CNode.data)
      k = k - 1
      if CNode.right:
         self.inorderrdfs(CNode.right,k)


   def inorderidfs(self, current, k):

      stack =[]
      c = current

      stack.append(c)
      while stack or c:
         while(c):
            stack.append(c)
            c = c.left

         if stack:
            c = stack.pop()

            k = k - 1
            if k == 0:
               print( c.data)

            c = c.right

   def remove(self, data):
      self.root = self.remove_recursively(self.root, data)

   def remove_recursively(self, current_node, data):
      if current_node is None:
         return current_node

      if data < current_node.data:
         current_node.left = self.remove_recursively(current_node.left, data)
      elif data > current_node.data:
         current_node.right = self.remove_recursively(current_node.right, data)
      else:
         if current_node.left is None:
            return current_node.right
         elif current_node.right is None:
            return current_node.left

         current_node.data = self.find_min(current_node.right)
         current_node.right = self.remove_recursively(current_node.right, current_node.data)

      return current_node

   def find_min(self, current_node):
      while current_node.left is not None:
         current_node = current_node.left
      return current_node.data
   def maxdepthdfs(self,current):
      if current is None:
         return 0

      res =  1 + max(self.maxdepthdfs(current.left), self.maxdepthdfs(current.right))
      return res
   def diameter(self,current):

      if not current:
         return 0
      return  max(self.diameter(current.left),self.diameter(current.right),self.maxdepthdfs(current.left) + self.maxdepthdfs(current.right) -1)



r = []

tree = BinarySearchTree()
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.insert(6)
tree.insert(7)
tree.insert(8)
h = 0
tree.inorderrdfs(tree.root,5)
print("In-order traversal:", r)
tree.inorderidfs(tree.root,5)
#diameter
#
# print(tree.diameter(tree.root))

