### Level 1:

## Delivery Service

The pizzeria's delivery guy Toma is delivering pizzas to the cyberpunktown of honor with an infinite two-dimensional
grid of houses.

He starts by delivering a pizza to the house at his starting location. Then, the pizzeria manager, back at the
restaurant, radios him directions for his next move. Each move is exactly one house to the north (^), south (v),
east (>), or west (<). After each move, he delivers another pizza to the house at his new location.

However, the manager has been a bit distracted by a kitchen mishap, so their directions aren't perfect. As a result, the
delivery guy ends up visiting some houses more than once. How many houses receive at least one pizza?

### Example:

- delivers pizzas to 2 houses: one at the starting location and one to the east.
- ^>v< delivers pizzas to 4 houses in a square, including twice to the house at his starting/ending location.
- ^v^v^v^v^v delivers a lot of pizzas to only 2 houses, making those residents very full.

### Question

How many houses receive at least one pizza?

## Solution

We use a simulation approach to find the unique house firt
Staring at origin (0,0) and move according to directions
At each step, we record the current position to ensure we count each house only once.
Updating position (x, y) based on the direction (^, v, <, >). and add the new point on the set
