def answer():
   def add_edge(f, t):
      if f not in graph:
         graph[f] = []
      if t not in graph:
         graph[t] = []
      graph[f].append(t)
   def dfs(start, target, visited,length):
      if start in visited:
         return

      if start == 6:
         return (length)

      visited.add(start)
      for i in graph[start]:


         return(dfs(i, target, visited, length + 1))

      visited.remove(start)
   graph ={}
   add_edge(1, 2)
   add_edge(2, 3)
   add_edge(2, 5)
   add_edge(3, 6)
   add_edge(6, 7)
   print(graph)
   target = 6
   visited = set()
   return(dfs(1, target, visited,0))

print(answer())