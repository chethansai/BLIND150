def a():
   n = [3,4,5,1,2]
   i = 0
   j = len(n)-1
   a = n[0]
   while(i<j):
      if(n[i]<n[j]):
         a =min(a,n[i])
         print(a)
         return
      m = (i + j)//2
      #left portion
      if(n[i]<=n[m]):
         i= m+1
      else:
         j= m+1
   print(n[i])


a()