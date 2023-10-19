def histogram():
   h = [2,1,5,6,2,3]
   a = 0
   s = []
   for i,height in enumerate(h):


      j = i
      while(s and s[-1][1] >h[j]):
         a = max(a,(i-j)*height)
         j+=1
         s.pop()
         s.append((i, h[j]))

      s.append((j, height))
   for i, height in s:
      a = max(a, (len(h) - i) * height)

   print(a)


histogram()