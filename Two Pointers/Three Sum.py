def summ():

   n = [-1,0,1,2,-1,-4]

   nn = sorted(n)
   print(nn)



   ans =[]
   for i,a in enumerate(nn):
      if(a<0 and a==nn[i-1]):
         continue
      l = i
      r = len(n) -1

      while(l<r):
         s = nn[i] + nn[l] + nn[r]
         if(s==0):
            ans.append([nn[l] , nn[r] , nn[i]])
            l =l+1
            r=r-1
         if(s<0):
            l = l+1
         if(s>0):
            r = r-1
         while(nn[l] == nn[l-1] and l<r):
            l = l + 1
   print(ans)



summ()