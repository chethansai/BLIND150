import heapq


def straight(h,g):

   if(len(h)%g > 0):
      return False

   #create min heap
   h_pairs = dict()
   heap = []
   for i in h:
      if i in h_pairs:
         h_pairs[i] = h_pairs[i] + 1
      else:
         h_pairs[i] = 1
   print(h_pairs)
   for i in h_pairs:

      heapq.heappush(heap, i)
   for i in range(len(h_pairs)):
      print(heapq.heappop(heap))

   while(len(heap)>0):
      start = heap[0]
      for i in range(start, start + g):
         if i not in h_pairs:
            return False
         h_pairs[i] = h_pairs - 1
         if(h_pairs[i] == 0):
            if(heap[0] != i):
               return False


            heapq.heappop(i)


   return True

def codejudge():
   hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
   groupSize = 3
   return (straight(hand, groupSize))
print(codejudge())