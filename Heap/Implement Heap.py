class Heap:
   def __init__(self):
      self.heap = [0]

   def push(self, n):
      self.heap.append(n)

      #percolate up
      #parent = i//2
      element = len(self.heap)-1
      parent = (len(self.heap)-1)//2
      while(self.heap[element] < self.heap[parent]):
         t = self.heap[element]
         self.heap[element] = self.heap[parent]
         self.heap[parent] = t

   def pop(self):
      if(len(self.heap) == 2):
         return (self.heap[1])
      if (len(self.heap) <= 1):
         return None
      i = 1
      element = self.heap[1]

      self.heap[1] = self.heap.pop()
      while(i * 2 <=len(self.heap) - 1):
         #descendents
         # i * 2
         # i * 2 + 1

         #right
         if((i * 2) + 1 <= len(self.heap)-1 and
            self.heap[(i * 2) + 1] < self.heap[i]  and
            self.heap[(i * 2) + 1] < self.heap[(i * 2)]
         ):
            t = self.heap[i]
            self.heap[i] = self.heap[(i * 2) + 1]
            self.heap[(i * 2) + 1] = t
            i = (i * 2) + 1

         #left
         elif (self.heap[(i * 2)] < self.heap[i]):
            t = self.heap[i]
            self.heap[i] = self.heap[(i * 2)]
            self.heap[(i * 2)] = t
            i = (i * 2)

         else:
            break
      return element

h = Heap()
h.push(2)
h.push(1)
h.push(3)
print(h.pop())




