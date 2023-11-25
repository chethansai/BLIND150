import sys

def answer():
    sys.setrecursionlimit(10**6)  # Adjust the limit as needed

    def dfs(r, c, rowm, columnc, current, ocean):
        # print(r,c)
        if r <= 0 or c <= 0 and ocean == "pacific":
            # print("true")
            return True
        if r >= len(grid) - 1 or c >= len(grid[0]) - 1 and ocean == "atlantic":

            return True
        if current < grid[r][c]:
            return False

        return(dfs(r + rowm, c + columnc, rowm, columnc, grid[r + rowm][c + columnc],ocean))
        # is_pacific_left = dfs(r, c - 1, grid[r][c])
        #
        # is_atlantic_bottom = dfs(r + 1, c, grid[r + 1][c])
        # is_atlantic_right = dfs(r, c + 1, grid[r][c])
        #
        # return is_pacific_top or is_pacific_left or is_atlantic_bottom or is_atlantic_right

    grid = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
    islands = 0

    def check(r, c):
        pacific = False
        atlantic = False
        if r <= 0 or c <= 0:
            return False

        else:
            pacific = False

        if r >= len(grid) - 1 or c >= len(grid[0]) - 1:
            return False
        else:
            atlantic = False
        if(not pacific):
            is_pacific_top = dfs(r, c, -1, 0, grid[r - 1][c],"pacific")
            is_pacific_left = dfs(r, c, 0, -1, grid[r][c - 1],"pacific")
            if is_pacific_top or is_pacific_left:
                pacific = True
            # print("is_pacific_top", is_pacific_top)
            # print("is_pacific_left", is_pacific_left)
        if(not atlantic):
            is_atlantic_bottom = dfs(r, c, 1, 0, grid[r + 1][c],"atlantic")
            is_atlantic_right = dfs(r, c, 0, 1, grid[r][c + 1],"atlantic")
            if is_atlantic_right or is_atlantic_bottom:
                atlantic = True

        #     print("is_atlantic_bottom", is_atlantic_bottom)
        #     print("is_atlantic_right", is_atlantic_right)
        #
        #
        # print("pacific",pacific)
        # print("atlantic",atlantic)

        return pacific and atlantic

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            # print(r,c)
            if(check(r, c)):
                print("check",r, c)




    return islands

print(answer())
