## Level 3:
### Go to the Location - 1
Patched into the city grid through your motorcycle's onboard diagnostics port, you discover a forecast for a massive
voltage storm brewing over the neon-drenched streets. Before you can assess if it might short-circuit your route, your
system suddenly powers down.

Your battery is dead.

To get back online, you'll need to charge it—but there’s a problem. The charging port at the cyberstation produces the
wrong voltage. Fortunately, you’re prepared: your saddlebag contains a collection of voltage adapters.

Each of your adapters is rated for a specific output voltage (your puzzle input line 1). An adapter can accept an input
voltage that is lower than its rating and still output its rated voltage.

Additionally, your motorcycle’s system includes a built-in charger rated for 3 volts higher than the highest-rated
adapter in your collection. (For instance, if your adapters are rated 3, 9, and 6 volts, the cycle would be rated for 12
volts.)

You decide to use all adapters you have at once to charge your battery + the motorcycle directly. The charging ports at
the cyberstation (your puzzle input line 2) are currently not occupied, so you plug in your adapters to the ports that
give the fastest charge (= highest voltage).

### Example:
Suppose your input contains those adapters and charging ports:

3, 6, 9
1, 2, 3, 4, 5, 6, 7, 8, 9
In this case, the highest-rated adapter is 9 volts, so the motorcycle can charge for 12 volts. You can use all three
adapters to charge your battery and the motorcycle directly with the following structure:

- adapter 3 uses port 3 (3 voltage) -> 3+3 = 6
- adapter 6 uses port 6 (6 voltage) -> 6+6 = 12
- adapter 9 uses port 9 (9 voltage) -> 9+9 = 18
- motorcycle uses port 8 (as 9 is occupied) -> 12+8 = 20
- Total voltage: 6 + 12 + 18 + 20 = 56

### Question
What is the total voltage output of the adapters and the motorcycle?
2443


