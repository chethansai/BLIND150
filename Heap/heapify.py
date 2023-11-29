def heapify():
   cur = (len(heapy) -1 )//2
   while(cur >= 0):
   #descendents
      i = cur
      while(i * 2 <= (len(heapy) - 1)):
         #right
         if((i * 2) + 1 <= (len(heapy) - 1)  and
               heapy[(i * 2) + 1] < heapy[i] and
               heapy[(i * 2) + 1] < heapy[i * 2]
         ):
            print('ds')
            t = heapy[(i * 2) + 1]
            heapy[(i * 2) + 1] = heapy[i]
            heapy[i] = t
            i = (i * 2) + 1


         #left
         elif(heapy[i * 2] < heapy[i]):
            print('dsds')
            t = heapy[i * 2]
            heapy[i * 2] = heapy[i]
            heapy[i] = t
            i = (i * 2)
         else:
            break

      cur -= 1
   print(heapy)

heapy = [60, 50, 80, 40, 30, 10, 70, 20, 90]


heapy.append(heapy.pop())
heapify()
