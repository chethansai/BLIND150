def dfs(g):
   if g in visit:
      answer.clear()
      return False

   if len(graph[g]) == 0:
      if g not in answer:
         answer.append(g)
      return True

   visit.add(g)
   for j in graph[g]:
      if(not dfs(j)):
         return False
   visit.remove(g)

   if g not in answer:
      answer.append(g)
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

answer = []
visit =set()
e = [[5,0],[4,0],[0,1],[0,2],[1,3],[3,2]]
# e =  [[3,1],[3,2],[1,0],[2,0]]
# e = [[1,0],[0,1]]
#prepare graph
graph = {}

print(ans())
print(answer)