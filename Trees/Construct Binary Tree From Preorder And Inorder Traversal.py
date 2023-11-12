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
         print(CNode.data)
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
def b(p,i):

   if len(p)  == 0 or len(i) == 0:
      return

   root = Node(p[0])

   mid = p.index( root.data)


   root.left = b(p[1 : mid +1 ],i[: mid+1])
   root.right = b(p[ mid + 1:], i[mid + 1:])
   return root


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
p = [3,9,20,15,7]
i = [9,3,15,20,7]


print(b(p,i))
bt = BinarySearchTree()
bt.root=b(p,i)
tree.inorder(bt.root)