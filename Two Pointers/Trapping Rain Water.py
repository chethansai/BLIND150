def trap():
   h = [0,1,0,2,1,0,1,3,2,1,2,1]
   l = 0
   ans = 0
   while(l<len(h)-1):
      a = 0
      r = l + 1
      while(r < len(h)):
         if(h[r] >= h[l]):
            ans = ans + a
            l = r
            break
         else:
            a +=  h[l] - h[r]
            r = r + 1
      if r == len(h):
         # If no taller bar was found to the right, move l one step to the right
         l += 1

   print(ans)
trap()