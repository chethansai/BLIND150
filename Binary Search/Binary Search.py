def bs():
   n = [-1,0,3,5,9,12]
   t = 12

   i = 0
   j = len(n)
   while(i<j):
      m = (i + j)//2
      if(n[m] == t):
         return m
      elif(n[m]>t):
         j = m
      else:
         i = m
   return False


print(bs())