def swm():
   n = [1,3,-1,-3,5,3,6,7]
   k = 3
   c_max = n[0]
   ans = []
   for i in range(0,len(n)-k+1):
      t_max = max(n[i:i+k])
      c_max = max(c_max,t_max)
      ans.append(c_max)

   print(ans)

swm()