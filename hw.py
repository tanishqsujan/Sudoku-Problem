def num_islands(grid):
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols:
            return
        if grid[r][c] == '0' or visited[r][c]:
            return

        visited[r][c] = True

        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and not visited[r][c]:
                dfs(r, c)
                count += 1  

    return count

grid = [
    "11000",
    "11000",
    "00100",
    "00011"
]

print("Number of islands:", num_islands(grid))