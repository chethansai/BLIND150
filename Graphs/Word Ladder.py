def bfs():
   q = []
   visited = set()
   q.append(beginWord)
   visited.add(beginWord)
   length = 0

   while(len(q) > 0):
      p = q.pop(0)
      #patterns
      if p == endWord:
         print('d')
         return True
      for i in range(len(p)):
         pattern = p[:i] + "*" + p[i+1:]
         print(pattern)

         for j in graph[pattern]:
            if j not in visited:


               q.append(j)
               visited.add(j)
      length += 1
   print(length)


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
wordList.append(beginWord)
# if endWord not in wordList:
#    return False
graph = {}
#build adjacency list
#n2
for i in wordList:
   print(i)
   #patters
   for j in range(len(i)):
      # print(j)
      pattern = i[:j] + "*" + i[j+1:]
      # print(pattern)
      if pattern not in graph:
         graph[pattern] = []
      graph[pattern].append(i)

print(graph)
print(bfs())
