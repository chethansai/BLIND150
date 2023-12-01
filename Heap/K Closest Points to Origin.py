import heapq


def closest(p, k):
   heap = []
   for i, j in p:
      distance = (i * i) + (j * j)
      heapq.heappush(heap, [distance, i, j])

   while(k > 0):
      heapq.heappop(heap)
      k = k - 1

   print(heapq.heappop(heap)[1:])









def codejudge():
   p = [[1,3],[-2,2]]
   k = 1
     #maxheap
   print(closest(p, k))

codejudge()
