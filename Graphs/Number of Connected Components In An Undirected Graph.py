


def answer():

   def bfs(i):
      q =[]
      q.append(i)
      while(len(q)>0):
         j = q.pop()

         for t in graph[j]:
            if(t not in visited):
               visited.append(t)
               q.append(t)

   ans = 0
   for i in graph:
      if i not in visited:
         ans = ans + 1

         bfs(i)
   print(ans)

edges = [[0, 1], [1, 2], [2, 3], [4, 5]]
graph = dict()
for f,t in edges:
   if f not in graph:
      graph[f] =[]
   if t not in graph:
      graph[t] =[]
   graph[f].append(t)
print(graph)

visited = []
answer()