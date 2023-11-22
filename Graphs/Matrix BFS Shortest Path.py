
def matrixx():
   matrix = [
      [0, 0, 0],
      [0, 1, 0],
      [1, 0, 0]
   ]
   matrix_r = len(matrix)
   matrix_c = len(matrix[0])
   visited = set()
   q = []
   q.append((0,0,0))
   visited.add((0,0))

   def bfs():

      while(len(q)>0):
         for i in range(len(q)):
            print(q)
            r, c, length = q.pop(0)
            print(r,c,length)

            #check if arrived at answer
            if (r == matrix_r - 1 and c == matrix_c - 1):
               return length
            if (r + 1  < 0        or c < 0        or
                r + 1  > matrix_r - 1 or c  > matrix_c - 1 or
                (r +1, c ) in visited or
               matrix[r + 1][c] == 1
            ):

               length = length + 0
            else:

               q.append((r+1,c,length + 1))
               visited.add((r+1,c))



            if (r   < 0        or c + 1 < 0        or
                r   > matrix_r - 1 or c + 1 > matrix_c - 1 or
                (r , c + 1) in visited or
               matrix[r][c + 1] == 1
            ):
               length = length + 0
            else:

               q.append((r,c + 1,length + 1))
               visited.add((r,c + 1))



            if (r - 1 < 0        or c < 0        or
                r - 1 > matrix_r - 1 or c > matrix_c - 1 or
                (r-1,c) in visited or
               matrix[r-1][c] == 0
            ):
               length = length + 0
            else:
               q.append((r-1,c,length + 1))
               visited.add((r-1,c))



            if (r  < 0        or c - 1 < 0        or
                r  > matrix_r - 1 or c -1 > matrix_c - 1 or
                (r, c -1) in visited or
               matrix[r][c-1] != 0
            ):
               length = length + 0
            else:
               q.append((r,c-1,length + 1))
               visited.add((r,c-1))



   return (bfs())

print(matrixx())