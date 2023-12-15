def merge(t, target):

   new_t = []
   for i in range(len(target)):
      print(i)
      print(target[i])

   for i in range(len(t)):
      print(t[i])
      c= 0
      for j in range(len(t[i])):
         # print(t[i][j])
         # print(target[j])
         if(t[i][j] > target[j]):
            continue
         else:
            c = c+1
      if(c ==3):
         new_t.append(t[i])
         print("fd",t[i])


   print(new_t)
   j =0
   counter = 0
   while(j<len(target)):

      for i in new_t:

         if(target[j] == i[j]):
            counter = counter + 1
            continue



      j = j + 1
   print(counter)
def codejudge():
   t = [[2, 5, 3], [1, 8, 4], [1, 7, 5]]
   target = [2,7,5]
   merge(t, target)

codejudge()
