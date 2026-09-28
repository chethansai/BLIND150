from collections import deque

def solve(board):
    rows, cols = len(board), len(board[0])
    q = deque()

    for r in range(rows):
        for c in range(cols):
            if (r in (0, rows - 1) or c in (0, cols - 1)) and board[r][c] == 'O':
                board[r][c] = 'S'
                q.append((r, c))

    while q:
        r, c = q.popleft()
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'O':
                board[nr][nc] = 'S'
                q.append((nr, nc))

    for r in range(rows):
        for c in range(cols):
            board[r][c] = 'O' if board[r][c] == 'S' else ('X' if board[r][c] == 'O' else board[r][c])
