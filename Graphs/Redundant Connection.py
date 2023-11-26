


def find(p):
   p = parents[p]
   #climb parent assignments
   while(p != parents[p]):
      #parent compression
      parents[p] = parents[parents[p]]
      p = parents[p]

   return(p)

def union(a, b):
   parent_a = find(a)
   parent_b = find(b)

   if(parent_a == parent_b):
      return False
   if(parent_a > parent_b):
      parents[b] = parent_a
      ranks[a] = ranks[a] + ranks[b]
   else:
      parents[b] = parent_a
      ranks[b] = ranks[a] + ranks[b]
   return True
def ans():


   for a, b in edges:

      if (not union(a, b)):
         print([a,b])
         return
edges = [[1,2],[1,3],[2,3]]
parents = [i for i in range(len(edges)+ 1) ]
ranks = [1] * (len(edges) + 1)
ans()