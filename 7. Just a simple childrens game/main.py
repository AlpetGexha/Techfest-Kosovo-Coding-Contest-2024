# read the input.txt file

input = open("input.txt", "r").read()


def simulate_flashes(grid, steps):
    rows, cols = len(grid), len(grid[0])
    total_flashes = 0

    # Helper function to process flashes
    def process_flashes():
        nonlocal total_flashes
        flashed = set()
        while True:
            new_flashes = False
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] > 9 and (r, c) not in flashed:
                        flashed.add((r, c))
                        total_flashes += 1
                        new_flashes = True
                        # Increase energy of neighbors
                        for dr in [-1, 0, 1]:
                            for dc in [-1, 0, 1]:
                                nr, nc = r + dr, c + dc
                                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in flashed:
                                    grid[nr][nc] += 1
            if not new_flashes:
                break
        # Reset flashed nodes
        for r, c in flashed:
            grid[r][c] = 0

    # Simulate the steps
    for _ in range(steps):
        # Increase energy levels
        for r in range(rows):
            for c in range(cols):
                grid[r][c] += 1
        # Process flashes
        process_flashes()

    return total_flashes


# Example grid
grid = [[4, 4, 3, 8, 6, 2, 4, 2, 6, 2],
        [6, 2, 6, 3, 2, 5, 1, 8, 6, 4],
        [2, 6, 1, 8, 8, 1, 2, 4, 3, 4],
        [2, 1, 3, 4, 2, 6, 4, 5, 6, 5],
        [1, 8, 1, 5, 1, 3, 1, 2, 4, 7],
        [2, 6, 1, 2, 4, 5, 7, 3, 2, 5],
        [8, 5, 8, 5, 7, 6, 7, 5, 8, 4],
        [7, 2, 1, 7, 1, 3, 4, 5, 5, 6],
        [2, 8, 2, 5, 4, 5, 6, 5, 6, 3],
        [8, 2, 4, 8, 4, 7, 3, 5, 8, 4] ]

# Simulate 100 steps
steps = 100
result = simulate_flashes(grid, steps)
print(f"Total flashes after {steps} steps: {result}")
