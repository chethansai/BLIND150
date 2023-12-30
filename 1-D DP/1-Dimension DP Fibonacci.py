#Fibnocci Bottom Up
def fibnoccibottomup(n):
   if(n <= 1):
      return n
   cache =[0, 1]
   i = 2
   while(i <= n):
      temp = cache[1]
      cache[1] = cache[0] + cache[1]
      cache[0] = temp
      i = i + 1
   return cache[1]
#Fibnocci Top Down
def fibnoccitopdown(n, cache):
   if(n <= 1):
      return n
   if n in cache:
      return cache[n]
   cache[n] = fibnoccitopdown(n - 1, cache) + fibnoccitopdown(n - 2, cache)
   return cache[n]
#FIBNOCCI Recursive
def fibnoccirecursive(n):
   if(n <= 1 ):
      return n
   return (fibnoccirecursive(n - 1) + fibnoccirecursive(n - 2))

def codejudge():
   n = 6
   #return (fibnoccirecursive(n))
   # cache = dict()
   # return (fibnoccitopdown(n, cache))
   return (fibnoccibottomup(n))
print(codejudge())
#0112358