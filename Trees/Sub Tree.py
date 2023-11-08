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
def subtree(tree1,tree2):
   if not tree1:
      return True
   if not tree2:
      return False

   if(sametree(tree1,tree2)):
      return True
   return (subtree(tree1.left,tree2) or subtree(tree1.right,tree2))


def sametree(tree1, tree2):

   if(not tree1 and not tree2):
      return True

   if(tree1 and tree2 and tree1.data and tree2.data):
      return sametree(tree1.left, tree2.left) and sametree(tree1.right, tree2.right)
   else:
      return False



tree1 = BinarySearchTree()
tree1.insert(3)
tree1.insert(4)
tree1.insert(5)
tree1.insert(1)
tree1.insert(2)

tree2 = BinarySearchTree()
tree2.insert(1)
tree2.insert(4)
tree2.insert(2)




print(subtree(tree1.root, tree2.root))