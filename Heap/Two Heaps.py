#two required
#median , sort , middle
#odd middle
#evenm two middle/2
#sort nlogn
#sorted 0(1)
#stream of values
#sort not easy as sort each time
#new value (N)
#getting value(1)
#push logN
#get O(1)
#2heaps small(maxHeap), large half(minHeap)
#small values <= large heap

#4, 7, 3, 5, 1
#4 - insert into any for first(small)
#7 - to large as otherwise differnce >= 2
# if equal number of elements - both/2
# otherwise  middle

#4, 2, 3, 5, 1
#if it was 2 instead of 7, then we would put it into small-> Since large condition fails > 4
#but equilibrium breaks, as otherwise differance >= 2
# so push 4 to other side.

#put into small always
#2 conditions
#All Left <= Right
#size differnce <2
   #if not pop from the smallest add. log n log n
#odd - Large size heap is median
#even - both/2
import heapq


def heapify(i):
   #add to small first
      #max heap handle
   i = -1 * i
   heapq.heappush(small, i)



   #small =< large
   if(small and
      large and
         ((small[0] * -1) > large[0])
   ):
      heapq.heappush(large, heapq.heappop(small) * -1)




   #size difference < 2
   if(len(small) > len(large) + 1):
      heapq.heappush(large,heapq.heappop(small) * -1)
   if(len(large) > len(small) + 1):
      heapq.heappush(small,heapq.heappop(large))


   #median
def median():
   #odd
   if(len(small) > len(large)):
      print('median',end='')
      print(small[0] * -1)
   elif(len(large) > len(small)):
      print('median',end='')
      print(large[0])
   #even
   else:
      print('median',end='')
      print(((small[0] * -1 )+ large[0])/2)

#executor
l = [4, 7, 3, 5, 1]
#initite two heaps
small = []
large = []
for i in l:
   print('i',end='')
   print(i)
   heapify(i)
   print('small',end='')
   print(small)
   print('large',end='')
   print(large)
   median()



