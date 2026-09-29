stack stores indices of temperatures that are still waiting for a warmer day. When temperatures[i] is warmer than the temperature at stack[-1], that index is popped and the number of waiting days is i - prev.

def dt():
   t = [73,74,75,71,69,72,76,73]
   ans = [0] * len(t)
   for i,v in enumerate(t):
      print(i,v)
      n = 0
      b = 0
      while(n+i<len(t)):
         if(t[n+i]>v):
            ans[i] = n
            break
         n +=1
   print(ans)

dt()
