

def addRooms(r, c):
   if (
         min(r, c) < 0
         or r == ROWS
         or c == COLS
         or (r, c) in visit
         or rooms[r][c] == -1
   ):
      return
   visit.add((r, c))
   q.append([r, c])
rooms =[[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
ROWS, COLS = len(rooms), len(rooms[0])
visit = set()
q = []

for r in range(ROWS):
   for c in range(COLS):
      if rooms[r][c] == 0:
         q.append([r, c])
         visit.add((r, c))

dist = 0
while q:
   for i in range(len(q)):
      r, c = q.pop(0)
      rooms[r][c] = dist
      addRooms(r + 1, c)
      addRooms(r - 1, c)
      addRooms(r, c + 1)
      addRooms(r, c - 1)
   dist += 1

print(rooms)