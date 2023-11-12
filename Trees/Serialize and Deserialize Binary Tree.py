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
class a:
   def deserialize(self):
      p = ['1', '2', 'N', 'N', '3', '4', 'N', 'N', '5', 'N', 'N']
      self.i = 0
      def dfs():

         if(p[self.i] == 'N'):
            self.i +=1
            return
         root = Node(int(p[self.i]))
         self.i = self.i + 1
         root.left = dfs()
         root.right = dfs()
         return root
      dfs()


r = []

tree = BinarySearchTree()
tree.insert(5)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(3)

h = 0
tree.inorder(tree.root)
print("In-order traversal:", r)

# Remove a node
tree.remove(4)
r = []
h = 0
tree.inorder(tree.root)
print("In-order traversal after removing 4:", r)


i = 0
# while(i <= len(p)):
#    root = Node(p[i])
#    if(p[i+1] == 'N' and p[i+2] == 'N'):
#       i = i+3
#    else:
#       if(p[i+1] != 'N' ):
#          root.left = p[i+1]
#       if(p[i + 2] != 'N'):
#          root.right = p[i+2]
aa = a()
print(aa.deserialize())
