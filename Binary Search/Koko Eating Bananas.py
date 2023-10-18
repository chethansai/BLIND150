import math
def koko():
   p = [3,6,7,11]
   h = 8

   j = max(p)
   i = 1

   while(i<=j):
      m = (i + j)//2
      a = 0
      for pile in p:


         a += math.ceil(pile/m)
      if(a==h):
         return m
      elif(a>h):
         i = m
      else:
         j = m





print(koko())