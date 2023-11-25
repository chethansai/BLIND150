



def answer():
   grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
   rotten = 0
   total = 0
   q = []
   rotten = 0
   for r in range(len(grid)):
      for c in range(len(grid[0])):
         if(grid[r][c] == 2):
            rotten += 1
            q.append((r,c))
         if (grid[r][c] != 0):
            total += 1
   ans = 0

   while(len(q) > 0):
      for i in range(len(q)):
         print(q)
         r, c = q.pop(0)


         directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
         for row_moment, column_moment in directions:
            row = r + row_moment
            column = c + column_moment

            if(row >= 0 and column >= 0 and
               row <len(grid) and column < len(grid[0]) and
               grid[row][column] == 1
              ):

               q.append((row, column))
               grid[row][column] = 2
               rotten += 1

      ans += 1
   print(ans,'ans')
   print(total,"total")
   print(rotten, "rotten")
   return ans if total == rotten else -1





print(answer())