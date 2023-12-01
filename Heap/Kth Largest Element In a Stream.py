import heapq


def answer():
   h = []
   k = 2
   for i in n:
      heapq.heappush(h, (-1 * i))
   while(k>0):
      heapq.heappop(h)
      k = k - 1
   s = heapq.heappop(h) * -1
   print(s)


n = [4, 5, 5, 8, 8]

answer()

