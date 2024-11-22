### Level 4

## Go to the location - 2

Somethings wrong, your motorcycle nevertheless broke because of the wrong voltage... Darn, some adapter must have been wrong. You still want to go there yo you switch to public transport - the cyberbus. But you have different lines to take and there are people waiting for different lines. Arriving early at the station you can look at the cyberbus's advanced seat allocation system, which relies on predictable rules based on the behavior of passengers. While waiting, you decide to figure out the best seat to ensure a comfortable ride.

The cyberbus seating layout is displayed as a grid. Each position is either floor (.), an empty seat (O), or an occupied seat (X). For example, the initial layout might look like this:

```
O.OO.OO.OO
OOOOOOO.OO
O.O.O..O..
OOOO.OO.OO
O.OO.OO.OO
O.OOOOO.OO
..O.O.....
OOOOOOOOOO
O.OOOOOO.O
O.OOOOO.OO
```

Now, you just need to model the passengers who will be boarding the cyberbus shortly. Fortunately, passengers are entirely predictable and always follow a simple set of rules. Their decisions depend on the number of occupied seats adjacent to a given seat (one of the eight positions immediately up, down, left, right, or diagonal). The following rules are applied to every seat simultaneously:

- If a seat is empty (O) and no adjacent seats are occupied, the seat becomes occupied.
- If a seat is occupied (X) and four or more adjacent seats are also occupied, the seat becomes empty.
- Otherwise, the seat's state does not change.
- Floor (.) never changes; passengers don't move seats to the floor, and no one sits there.

For example, after one round of these rules, every seat in the cyberbus's layout becomes occupied:

```
X.XX.XX.XX
XXXXXXX.XX
X.X.X..X..
XXXX.XX.XX
X.XX.XX.XX
X.XXXXX.XX
..X.X.....
XXXXXXXXXX
X.XXXXXX.X
X.XXXXX.XX
```

After a second round, the seats with four or more occupied adjacent seats become empty again:

```
X.OO.OX.XX
XOOOOOO.OX
O.O.O..O..
XOOO.OO.OX
X.OO.OO.OO
X.OOOOX.XX
..O.O.....
XOOOOOOOOX
X.OOOOOO.O
X.XOOOO.XX
```

This process continues for three more rounds:

```
X.XX.OX.XX
XOXXXOO.OX
O.X.X..X..
XOXX.XX.OX
X.XX.OO.OO
X.XXXOX.XX
..X.X.....
XOXXXXXXOX
X.OOXXXO.O
X.XOXXX.XX

X.XX.OX.XX
XOXXXOO.OX
O.X.X..X..
XOXX.XX.OX
X.XX.OO.OO
X.XXXOX.XX
..X.X.....
XOXXXXXXOX
X.OOXXXO.O
X.XOXXX.XX

X.XO.OX.XX
XOOOXOO.OX
O.X.O..X..
XOXX.XX.OX
X.XO.OO.OO
X.XOXOX.XX
..O.O.....
XOXOXXOXOX
X.OOOOOO.O
X.XOXOX.XX
```

At this point, something interesting happens: the chaos stabilizes and further applications of these rules cause no seats to change state! Once people stop moving around, you count 37 occupied seats.

Question
Simulate your seating area by applying the seating rules repeatedly until no seats change state to select the bus to take. How many seats end up occupied?

## Solution

To solve the problem, we need to simulate the behavior of passengers repeatedly applying the seating rules until the layout stabilizes and no seats change state. Here's the step-by-step approach:

Steps:
Input Parsing: Represent the seating layout as a 2D grid. Each cell is either O (empty seat), X (occupied seat), or . (floor).

Rules Application:
If a seat is empty (O) and no adjacent seats are occupied, it becomes occupied (X).

If a seat is occupied (X) and four or more adjacent seats are occupied, it becomes empty (O).

Floor (.) never changes.
