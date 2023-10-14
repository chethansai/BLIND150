def encode():
   s = ["lint", "code", "love", "you"]
   res =''
   for i in s:
      code = i + str(len(s)) + "/"
      res += code
   return res


def decode(ss):

   ans =[]
   l = 0
   e = 0
   while (l<len(ss)):

      if(ss[l] == '/'  ):
         print('printing')
         print(l - e - 1)
         print(l)
         print(e)
         print(ss[l - 1])
         if(ss[l - 1] == str(l -e -1)):
            print('print')
            print(ss[e:l-1])
            ans.append(ss[e:l-1])

         e = l +1
      l=l+1
   print(ans)

ss = encode()
print(ss)
decode(ss)
