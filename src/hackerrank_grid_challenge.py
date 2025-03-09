def grid_challenge(grid):
    n = len(grid)
    sorted_grid = ["".join(sorted(row)) for row in grid]

    for col in range(n):
        for row in range(1, n):
            if sorted_grid[row][col] < sorted_grid[row - 1][col]:
                return "NO"
    return "YES"
