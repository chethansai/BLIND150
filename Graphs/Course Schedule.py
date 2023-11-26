def dfs(g):
   if g in visit:
      return False
   if len(graph[g]) == 0:
      return True

   visit.add(g)
   for j in graph[g]:
      if(not dfs(j)):
         return False
   visit.remove(g)

   graph[g] = []
   return True

def ans():
   for f, t in e:
      if f not in graph:
         graph[f] = []
      if t not in graph:
         graph[t] = []
      graph[f].append(t)


   for g in graph:
      if(not dfs(g)):
         return False
   return True


visit =set()
e = [[0, 1], [0, 2], [1, 3], [1, 4],[3, 4]]
#prepare graph
graph = {}
print(ans())
