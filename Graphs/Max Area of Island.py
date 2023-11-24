def answer():
   def bfs(r, c):
      q = []

      q.append((r,c))

      while(len(q)>0):
         r, c = q.pop()

         directions = [(1, 0),(-1, 0), (0, -1), (0, 1)]
         for row_moment, column_moment in directions:

            row    = r + row_moment
            column = c + column_moment

            if(
               row >= 0        and
               column >= 0     and

               row <= len(grid) - 1 and
               column <= len(grid[0]) - 1 and

               (row, column) not in visited and

               grid[row][column] == 1

            ):

               visited.add((row, column))
               q.append((row,column))

   grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
   islands = 0

   visited = set()
   maxarea = 0
   for r in range(len(grid)):
      for c in range(len(grid[0])):
         if grid[r][c] == 1 and (r,c) not in visited:
            a = len(visited)
            bfs(r,c)
            b = len(visited)
            currentarea = b - a
            print(b,a)
            print(currentarea)
            print()
            maxarea = max(maxarea, currentarea)
   return maxarea





print(answer())