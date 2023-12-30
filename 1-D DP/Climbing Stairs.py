#Stairs Top Down
def stairstd(n, cache):
   if(n <= 2):
      return n
   if n in cache:
      return cache[n]
   cache[n] = stairstd(n - 1, cache) + stairstd(n - 2, cache)
   return cache[n]

#stairs bottom up
def stairsbu(n):

   i = 2
   ans = 2
   cache = [1,2]
   while(i <= n):
      temp = cache[1]
      cache[1] = cache[0] + cache[1]
      cache[0] = temp

      i = i + 1
   return cache[1]

def codejudge():
   n = 5
   cache = dict()
   # return(stairstd(n,cache ))
   return(stairsbu(n))

print(codejudge())