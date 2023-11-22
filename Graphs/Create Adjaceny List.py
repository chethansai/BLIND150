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

answer()