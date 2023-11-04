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

   def inorder(self, CNode):
      if CNode.left:
         self.inorder(CNode.left)
      if CNode.data:
         r.append(CNode.data)
      if CNode.right:
         self.inorder(CNode.right)

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

      res =  1 + max(self.maxdepthdfs(  res))
   def maxdepthbfs(self):
      a = []
      if not self.root:
         return 0
      a.append(self.root)
      ans = 0
      while(len(a) > 0):
         for i in range(len(a)):
            print('a')
            c = a.pop(0)

            if (c.left):
               a.append(c.left)
            if (c.right):
               a.append(c.right)
         ans += 1


      return ans

   def maxdepthidfs(self):


      if self.root is None:
         return 0
      s = []
      s.append(self.root)
      while(s):
         c = s.pop()
         print(c.data)
         if (c.left):
            s.append(c.left)
         if (c.right):
            s.append(c.right)


r = []

tree = BinarySearchTree()
tree.insert(5)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(3)
tree.insert(15)
tree.insert(17)
tree.insert(12)
tree.insert(14)
tree.insert(13)

h = 0
tree.inorder(tree.root)
print("In-order traversal:", r)

# Remove a node
tree.remove(4)
r = []
h = 0
tree.inorder(tree.root)
print("In-order traversal after removing 4:", r)
res = 0
print(tree.maxdepthdfs(tree.root))
print(tree.maxdepthbfs())
tree.maxdepthidfs()