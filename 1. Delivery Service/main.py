input = open("input.txt", "r").read()

def unique_houses_visited(directions):
    # Starting position
    x, y = 0, 0
    visited = {(x, y)}  # Set to track unique positions

    # Map each direction to a movement
    moves = {'^': (0, 1), 'v': (0, -1), '>': (1, 0), '<': (-1, 0)}

    # Process each direction
    for direction in directions:
        dx, dy = moves[direction]
        x += dx
        y += dy
        visited.add((x, y))

    return len(visited)


result = unique_houses_visited(input)
print(result)
