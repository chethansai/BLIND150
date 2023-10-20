def mi():
   s = "ADOBECODEBANC"
   t = "ABC"

   d1, d2 = {},{}
   for i in range(0, len(t)):
      print(t[i])
      d1[t[i]] = d1.get(t[i], 0) + 1
   l = 0
   ans = ''
   l_ans = 0
   have = 0
   for i in range(0, len(s)):

      d2[s[i]] = d2.get(s[i], 0) + 1
      if(s[i] in d1 and d1[s[i]]==d2[s[i]]):

         have +=1
      while(have == len(d1)):
         if( len(ans) >( i-l +1 ) ):
            ans_l=[l,i]
            ans = s[l:i+1]

         d2[s[l]] -= 1
         if s[l] in d1 and d2[s[l]] < d1[s[l]]:
            have -= 1

         l+=1



   print(ans)


   # print(d1,d2)


mi()