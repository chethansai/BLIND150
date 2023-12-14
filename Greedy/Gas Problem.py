
def gas(g, c):
   s_g = 0
   s_c = 0
   for gases in g:
      s_g += gases
   for costs in c:
      s_c += costs
   print(s_g, s_c)
   if(s_g < s_c):
      return False
   diff = []
   for a in range(0, len(g)):
      print(a)
      diff.append(g[a] - c[a])
   print(diff)

   total = 0
   ans = 0
   for d in range(0,len(diff)):

      total += diff[d]
      if(total < 0):
         total = 0
         ans = d + 1
   return ans






def codejudge():
   g = [1, 2, 3, 4, 5]
   c = [3, 4, 5, 1, 2]
   return (gas(g, c))
print(codejudge())