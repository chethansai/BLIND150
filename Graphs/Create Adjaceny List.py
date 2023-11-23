def answer():
   def add_edge(f, t):
      if f not in graph:
         graph[f] = []
      if t not in graph:
         graph[t] = []
      graph[f].append(t)

   graph ={}
   add_edge(1, 2)
   add_edge(1, 3)
   add_edge(2, 4)
   add_edge(2, 5)
   add_edge(3, 6)
   add_edge(3, 7)
   print(graph)

class Node:
   def __init__(self, value):
      self.value = value
      self.neighbours = []
def answer1():
   def add_edge1(i,j):
      if i not in graph:
         copy_i = Node(i)
      else:
         copy_i = graph[i]
      if j not in graph:
         copy_j = Node(j)
      else:
         copy_j = graph[j]
      copy_i.neighbours.append(copy_j)
      copy_j.neighbours.append(copy_i)

   def print_graph_from_root(root):
     visited = set()

     def dfs(node):
         if node not in visited:
             print(node.value, end=' ')
             visited.add(node)
             for neighbor in node.neighbours:
                 dfs(neighbor)

     dfs(root)



   graph ={}
   adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]
   root = Node(adjList[0][0])
   graph[adjList[0][0]] = root
   for i, j in adjList:
      add_edge1(i, j)

   print_graph_from_root(root)
answer()
answer1()