class Node:
   def __init__(self, value):
      self.value = value
      self.neighbours = []
def answer():
   def dfs(i):
      if i not in adjList:
         copy = Node(i)
         oldtonew.append(copy)
         for neighbour in adjList[i]:
            copy.neighbours.append(dfs(neighbour))
   adjList = [[2,4],[1,3],[2,4],[1,3]]
   oldtonew = {}

   for i in adjList:
      dfs(i)


answer()

