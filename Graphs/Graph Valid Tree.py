




def dfs(c, p):
   if c in visited :
      return False
   visited.add(c)
   for i in graph[c]:
      if i == p:
         continue
      if not dfs(i,c):
         return False
   return True
n = 3
edges = [[0, 1], [1, 2]]
graph = {}
for f, t in edges:
   if f not in graph:
      graph[f] = []
   if t not in graph:
      graph[t] = []
   graph[f].append(t)
   graph[t].append(f)

visited = set()
print(graph)
if(dfs(0, -1) and len(visited)== n):
   print('True')
else:
   print(len(visited))
   print('False')