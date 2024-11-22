### Level 7

## Just a simple childrens game

You respond quickly to the mysterious caller, asking to be connected to a particular runner. After a moment, your request is accepted, and a faint buzzing sound fills the line. Eventually, a calm, confident female voice greets you.

You explain the situation: this looting game she's been pulled into is a dangerous endeavor. If she wins, she’ll end up with all the digital loot, making her a prime target for other runners and factions.

To your surprise, she seems confused. She has no knowledge of any such game. Her reaction leaves you unsettled, strange possibilities flickering through your mind. Taking a leap of faith, you ask her to meet you at the cyberstation. After a brief hesitation, she agrees.

You arrive at the cyberstation. Amidst the hum of neon lights and the clatter of automated trains, a woman with jet-black hair and a red jacket waits by the terminal. She introduces herself as Lara.

You share what you know about the looting challenge. She listens intently, intrigued rather than alarmed. She then reveals something curious: a few days ago, she received a cryptic message from an unknown source. The sender urged her to trust them and promised that the meaning of the message would become clear in time.

Fascinated, you ask her to show you the message. She pulls out a small, strange device—its buttons flicker erratically with colorful lights. A rush of nostalgia hits you as you recognize the gadget. It’s an old puzzle game you once played with friends as a kid.

The stakes are high, but before you can proceed further, you need to figure out how to decode the message hidden within this game-like interface. Time to unlock the secrets of the device and uncover the truth behind this mysterious challenge.

The device in Lara’s hand hums softly as you examine it. Its interface suddenly displays a grid of flickering lights, reminding you of something from an old arcade. You realize it’s not just a puzzle—it’s a live feed from a network of interconnected nodes, representing energy surges in a hidden grid-like system.

The display shows 100 nodes, neatly arranged in a 10 by 10 grid. Each node, like a circuit under strain, slowly builds up energy over time. When a node's energy reaches a critical threshold, it flashes brightly, releasing energy into neighboring nodes and causing chain reactions.

If you can predict when and where these energy surges occur, you might be able to decipher the message hidden in the device. But there’s a catch: triggering too many surges at the wrong time could overload the system, erasing the message entirely.

Fortunately, the device allows you to monitor the energy levels of each node. Here's an example of what the grid might look like:

```
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
```

The device’s screen reveals a more detailed view of the grid. Each node displays an energy level between 0 and 9. For instance, the top-left node currently shows a level of 5, while the bottom-right one sits at 6. The numbers might look random, but the grid is alive with activity, and every step brings cascading changes.

To decode the message, you realize you must model the behavior of the system step by step. Here’s what happens during each step:

- Energy Increase: Every node on the grid increases its energy level by 1.
- Flashing: Any node whose energy level exceeds 9 releases a burst of energy, or "flashes."

  - This flash boosts the energy level of all adjacent nodes by 1, including diagonal neighbors.
  - If any of these adjacent nodes exceed an energy level of 9, they also flash.
  - This chain reaction continues until no new flashes occur.

- Reset: After flashing, an node’s energy level resets to 0 as it expends all its energy.

Each node can flash only once per step, even if it is affected by multiple flashes.

Example Chain Reaction
To understand the mechanics, consider this scenario with a middle octopus surrounded by neighbors:

```

Before any steps:
11111
19991
19191
19991
11111

After step 1:

34543
40004
50005
40004
34543

After step 2:


45654
51115
61116
51115
45654
```

Here is how the larger example above progresses:

```
Before any steps:

5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526


After step 1:

6594254334
3856965822
6375667284
7252447257
7468496589
5278635756
3287952832
7993992245
5957959665
6394862637

After step 2:
8807476555
5089087054
8597889608
8485769600
8700908800
6600088989
6800005943
0000007456
9000000876
8700006848

After step 3:
0050900866
8500800575
9900000039
9700000041
9935080063
7712300000
7911250009
2211130000
0421125000
0021119000

After step 4:
2263031977
0923031697
0032221150
0041111163
0076191174
0053411122
0042361120
5532241122
1532247211
1132230211

After step 5:
4484144000
2044144000
2253333493
1152333274
1187303285
1164633233
1153472231
6643352233
2643358322
2243341322

After step 6:
5595255111
3155255222
3364444605
2263444496
2298414396
2275744344
2264583342
7754463344
3754469433
3354452433

After step 7:
6707366222
4377366333
4475555827
3496655709
3500625609
3509955566
3486694453
8865585555
4865580644
4465574644

After step 8:
7818477333
5488477444
5697666949
4608766830
4734946730
4740097688
6900007564
0000009666
8000004755
6800007755

After step 9:
9060000644
7800000976
6900000080
5840000082
5858000093
6962400000
8021250009
2221130009
9111128097
7911119976

After step 10:
0481112976
0031112009
0041112504
0081111406
0099111306
0093511233
0442361130
5532252350
0532250600
0032240000
```

After step 10, there have been a total of 204 flashes. Fast forwarding, here is the same configuration every 10 steps:

```
After step 20:
3936556452
5686556806
4496555690
4448655580
4456865570
5680086577
7000009896
0000000344
6000000364
4600009543

After step 30:
0643334118
4253334611
3374333458
2225333337
2229333338
2276733333
2754574565
5544458511
9444447111
7944446119

After step 40:
6211111981
0421111119
0042111115
0003111115
0003111116
0065611111
0532351111
3322234597
2222222976
2222222762

After step 50:
9655556447
4865556805
4486555690
4458655580
4574865570
5700086566
6000009887
8000000533
6800000633
5680000538

After step 60:
2533334200
2743334640
2264333458
2225333337
2225333338
2287833333
3854573455
1854458611
1175447111
1115446111

After step 70:
8211111164
0421111166
0042111114
0004211115
0000211116
0065611111
0532351111
7322235117
5722223475
4572222754

After step 80:
1755555697
5965555609
4486555680
4458655580
4570865570
5700086566
7000008666
0000000990
0000000800
0000000000

After step 90:
7433333522
2643333522
2264333458
2226433337
2222433338
2287833333
2854573333
4854458333
3387779333
3333333333

After step 100:
0397666866
0749766918
0053976933
0004297822
0004229892
0053222877
0532222966
9322228966
7922286866
6789998766
```

After 100 steps, there have been a total of 1656 flashes.

Given the starting energy levels of the nodes on your device, simulate 100 steps.

### Question

How many total flashes are there after 100 steps?
