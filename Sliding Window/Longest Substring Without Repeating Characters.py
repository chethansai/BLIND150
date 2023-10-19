def sub():
   s = "abcabcbb"
   d = dict()
   a = 0
   start = 0
   for i in range(0,len(s)):
      if(s[i] in d and start <= d[s[i]]):
         start = d[s[i]] +1
      else:

         a = max(a,i - start + 1 )
      d[s[i]] = i
   print(a)
sub()