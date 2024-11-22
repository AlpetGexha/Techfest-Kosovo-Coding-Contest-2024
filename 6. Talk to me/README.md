### Level 6

## Talk to me

You enter the number and listen to the response. A cryptic transmission comes through your secure channel. It’s from a
rogue faction of netrunners in the undercity calling themselves "The Circles." They’ve intercepted plans for an
underground exchange, but it seems like the participants have a twisted way of distributing loot.

They mistake you for their operator and the curiosity mixes with opportunity for you. The voice on the other end
explains the brutal setup of success to you:

- Every runner brings a stash of loot. They all sit in a circle, each assigned a position starting with 1.
- Starting with the first runner, they take turns stealing all the loot from the runner directly to their left.
- A runner with no loot is booted from the circle and skips their turn.
  For example, if there are five runners (numbered 1 to 5):

  1
  5 2
  4 3

- Runner 1 takes Runner 2's stash.
- Runner 2 is out of loot and skipped.
- Runner 3 takes Runner 4's stash.
- Runner 4 is out of loot and skipped.
- Runner 5 takes Runner 1's two stashes.
- Runner 1 and Runner 2 are both out, so they’re skipped.
- Runner 3 takes Runner 5's three stashes.

With five runners, Runner 3 ends up with all the loot.

Question
Given the number of runners (from your puzzle input), which one walks away with the entire stash? Time to decode the
chaos and find out who will be the person you need to follow for the biggest opportunity.

### Solution

This problem is a variant of the **Josephus Problem**, which involves finding the last remaining person after a series of eliminations in a circle.

For this specific problem, we need to determine the position of the last remaining runner given n runners. The Josephus problem has a formulaic solution for when every second person is eliminated, which applies here.

```
J(n) = 2 * (n - (n-2^L) + 1 )
```
