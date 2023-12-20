def partition(a):
   print(a)

   o = {}
   for i, v in enumerate(a):
      # print(i, v)
      o[v] = i
   print(o)

   end = 0
   ans = []
   size = 0
   for i in range(0, len(a)):
      # print(i)
      end = max(end,o[a[i]])
      size += 1
      if(end == i):
         ans.append(size)
         size = 0

   print(ans)





def codejudge():
   a = 'ababcbacadefegdehijhklij'
   partition(a)

codejudge()