def stocks():
   p = [7,1,5,3,6,4]
   l = p[0]
   a = 0
   for i in p:
      if(l>i):
         l = i
      a = max(a, i - l)
   print(a)

stocks()