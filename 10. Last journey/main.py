# read the input.txt file

input = open("input.txt", "r").read()

grid = input.split("\n")


# Input grid
# grid = [
#     "..##.......",
#     "#...#...#..",
#     ".#....#..#.",
#     "..#.#...#.#",
#     ".#...##..#.",
#     "..#.##.....",
#     ".#.#.#....#",
#     ".#........#",
#     "#.##...#...",
#     "#...##....#",
#     ".#..#...#.#",
# ]

def count_security_checks(grid, right, down):
    rows = len(grid)
    cols = len(grid[0])  # Width of the grid
    x, y = 0, 0  # Starting position
    security_checks = 0

    while y < rows:
        # Check for security measure
        if grid[y][x % cols] == '#':
            security_checks += 1
        # Move according to the slope
        x += right
        y += down

    return security_checks


# Calculate security checks for slope (right 3, down 1)
result = count_security_checks(grid, right=3, down=1)
print(result)
