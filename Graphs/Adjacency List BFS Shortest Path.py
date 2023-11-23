def answer():
   def add_edge(f, t):
      if f not in graph:
         graph[f] = []
      if t not in graph:
         graph[t] = []
      graph[f].append(t)

   def bfs(q, target, length, visited):


      while(len(q)>0):
         start,length = q.pop(0)

         if start == 7:
            return length
         for i in graph[start]:


            if i not in visited:
               q.append((i,length+1))
               visited.add(i)




   graph ={}
   add_edge(1, 2)
   add_edge(1, 3)
   add_edge(2, 4)
   add_edge(2, 5)
   add_edge(3, 6)
   add_edge(3, 7)
   print(graph)
   visited = set()
   q = []
   q.append((1,0))
   visited.add(1)
   return (bfs(q, 7, 0, visited))

print(answer())