### Level 10:

## Day 10: "Last journey"

With the access issues resolved, you set off toward the cyberport. Travel across the grid might be swift, but it’s far from safe. The grid is littered with security checks. You’ll need to calculate how many you will have to pass.

The security checks are strategically placed, appearing only on exact integer coordinates of the grid. You manage to obtain a map (your puzzle input) of the terrain, showing open squares (.) and security checks (#). For example:

```
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
```

These aren’t the only checks, though. Due to some arcane principle you vaguely recall about digital fractals and grid replication, the same pattern repeats infinitely to the right:

```
..##.........##.........##.........##.........##.........##.......  --->
#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........#.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...##....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
```

You begin your journey at the open square (.) in the top-left corner of the map, with the goal of navigating to the bottom (just beyond the last row on your map).

Your vehicle—a budget hover-sled—only supports specific travel slopes due to its limited navigation algorithm. Calculate the number of security checks (#) you would encounter following the slope of right 3, down 1:

From your starting point at the top-left, move 3 positions to the right and 1 position down. Repeat this pattern—right 3, down 1—until you pass beyond the bottom of the map.

In the example map, the positions you would traverse are marked as O for open squares and X for security measures:

```
..##.........##.........##.........##.........##.........##.......  --->
#..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........X.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...#X....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
```

In this scenario, following the path with a right 3, down 1 slope would lead you to encounter 7 security checkpoints.

### Question

Starting from the top-left corner of your grid and navigating with the same pattern (right 3, down 1), how many security measures will you trigger on your journey?

### Solution

To calculate how many security measures (#) you will encounter following the slope of "right 3, down 1"

Understand the Grid Expansion:

- The grid repeats infinitely to the right. If the width of the map is
𝑊 W, the position X to check in each row will be calculated as XmodW.

Traversal Pattern:

- Start at the top-left corner (row 0, column 0).
- Move right by 3 columns and down by 1 row.
- Stop when you move beyond the last row of the map.
- Count Security Checks (#):

For each step, check the character at the current position:

- If it is #, increment the counter.
- Otherwise, continue without incrementing.

Edge Handling:

- Use modulo arithmetic to wrap around the horizontal dimension.
