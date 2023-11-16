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

def treemaze(root):
   path = []
   def traversal(root,path):
      if not root:
         return False
      if root.data == 0:
         return False
      path.append(root.data)
      if root.data != 0 and not root.left and not root.right:
         return True


      traversal(root.left,path)
      traversal(root.right,path)

      path.pop()


   traversal(root,path)
   return(path)




def ans():
   a = [1, 2, 3]

   #ans is global
   ans = []
   tempans = []
   i = 0
   def subsets(i,a,ans,tempans):


      if (i>=len(a)):
         ans.append(tempans.copy())
         return

      # consider with element at index
      tempans.append(a[i])
      subsets(i+1,a, ans, tempans)
      tempans.pop()
      
      
      # consider without element at index
      subsets(i+1, a, ans, tempans)



   subsets(i,a,ans,tempans)
   print(ans)
tree = BinarySearchTree()

tree.insert(1)
tree.insert(2)
tree.insert(4)
tree.insert(3)
tree.insert(5)
print(treemaze(tree.root))

print(ans())
