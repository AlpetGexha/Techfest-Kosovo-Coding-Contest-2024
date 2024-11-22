input = open("input.txt", "r").read()


def count_occupied_seats(grid):
    rows, cols = len(grid), len(grid[0])

    def get_adjacent_occupied(r, c):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        count = 0
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 'X':
                count += 1
        return count

    while True:
        new_grid = [list(row) for row in grid]
        changes = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'O':  # Empty seat
                    if get_adjacent_occupied(r, c) == 0:
                        new_grid[r][c] = 'X'
                        changes += 1
                elif grid[r][c] == 'X':  # Occupied seat
                    if get_adjacent_occupied(r, c) >= 4:
                        new_grid[r][c] = 'O'
                        changes += 1

        if changes == 0:  # No changes, stabilization reached
            break

        grid = new_grid

    return sum(row.count('X') for row in grid)


initial_grid = input.split("\n")
# # Example input
# initial_grid = [
#     "O.OO.OO.OO",
#     "OOOOOOO.OO",
#     "O.O.O..O..",
#     "OOOO.OO.OO",
#     "O.OO.OO.OO",
#     "O.OOOOO.OO",
#     "..O.O.....",
#     "OOOOOOOOOO",
#     "O.OOOOOO.O",
#     "O.OOOOO.OO",
# ]


# Convert input to a list of lists
grid = [list(row) for row in initial_grid]

# Get the result
occupied_seats = count_occupied_seats(grid)
print(occupied_seats)
