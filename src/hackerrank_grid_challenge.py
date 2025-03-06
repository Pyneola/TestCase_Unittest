def grid_challenge(grid):
    sorted_grid = ["".join(sorted(row)) for row in grid]
    for col in range(len(sorted_grid[0])):
        if any(
            sorted_grid[row][col] > sorted_grid[row + 1][col]
            for row in range(len(sorted_grid) - 1)
        ):
            return "NO"
    return "YES"
