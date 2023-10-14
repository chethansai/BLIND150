def twosum():
   t = 9
   n = [2,7,11,15]

   l = 0
   r = len(n) -1
   while(l<r):

      if(n[l] + n[r] == t):
         return (str(l) + " " +str(r))
      if(n[l] + n[r] < t):
         l += 1
      if (n[l] + n[r] > t):
         r -= 1

      print( l, r)

twosum()