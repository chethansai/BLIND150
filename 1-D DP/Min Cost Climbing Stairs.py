#Stairs Top Down
def stairstd(n, c, cache):
   if(n == 0):
      return c[0]
   if n == 1:
      return c[1]
   print(cache)
   if n in cache:
      return cache[n]
   cache[n] = min(stairstd(n-1, c, cache), stairstd(n-2, c, cache)) + c[n]

   return cache[n]

#stairs bottom up
def stairsbu(n, c):


   if(c[0] < c[1]):
      cache = [c[1], c[0]]
      i = 1

   else:
      cache = [c[0], c[1]]
      i = 2
   print(cache)
   while(i <= n - 2):
      temp = cache[1]
      if(cache[1] + c[i] < cache[1] + c[i + 1]):
         cache[1] = cache[1] + c[i]
         i =i + 1
      else:
         cache[1] =  cache[1] + c[i + 1]
         i = i + 2
      cache[0] = temp
      print(i,c[i],c[i+1], cache)

   return cache[1]

def codejudge():
   n = 9

   cache = dict()
   c = [1,100,1,1,100,1,1,1,100,0]#0
   #    0  1  2 3  4  5 6 7   8 9
   # return(stairstd(n, c, cache ))

   return(stairsbu(n, c))

print(codejudge())