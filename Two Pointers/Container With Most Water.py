def most():
   h = [1, 8, 6, 2, 5, 4, 8, 3, 7]

   l = 0
   r = len(h) - 1
   a = 0
   while(l<r):

      aa = abs(r - l) * min(h[r],h[l])

      if(h[l]<h[r]):
         l = l + 1
      else:
         r = r - 1
      a = max(a,aa)
   print(a)








most()