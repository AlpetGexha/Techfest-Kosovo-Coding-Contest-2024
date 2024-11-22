### Level 9

## AI Navigation

The loot is secure, but the danger isn’t over yet. With a target painted squarely on your back, staying in the city
isn’t an option. You need a way out—fast.

Turning to the Beacon of Unity, an AI-powered navigation system rumored to calculate escape routes with surgical
precision, you send it a request for the safest path out of the chaos. Moments later, the beacon responds with a cryptic
transmission:

To decode the route, you must analyze the syntax provided. It consists of multiple lines of data, each representing
chunks. A chunk can contain other nested chunks, creating layers of complexity. These chunks follow a strict structure,
opening and closing with one of four specific pairs of matching characters:

- If a chunk opens with (, it must close with ).
- If a chunk opens with [, it must close with ].
- If a chunk opens with {, it must close with }.
- If a chunk opens with <, it must close with >.

So, () is a legal chunk that contains no other chunks, as is []. More complex but valid chunks
include ([]), {()()()}, <([{}])>, [<>({}){}[([])<>]], and even (((((((((()))))))))).

Some lines are incomplete, but others are corrupted. Find and discard the corrupted lines first.

A corrupted line is one where a chunk closes with the wrong character - that is, where the characters it opens and
closes with do not form one of the four legal pairs listed above.

Examples of corrupted chunks include (], {()()()>, (((()))}, and <([]){()}[{}]). Such a chunk can appear anywhere within
a line, and its presence causes the whole line to be considered corrupted.

For example, consider the following navigation subsystem:

[({(<(())[]>[[{[]{<()<>>

[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>

(((({<>}<{<{<>}{[]{[]{}

[[<[([]))<([[{}[[()]]]

[{[{({}]{}}([{[{{{}}([]

{<[[]]>}<{[{[{[]{()[[[]

[<(<(<(<{}))><([]([]()

<{([([[(<>()){}]>(<<{{

<{([{{}}[<[[[<>{}]]]>[]]

Some of the lines aren't corrupted, just incomplete; ignore those lines. The remaining five lines are corrupted:

{([(<{}[<>[]}>{[]{[(<()> - Expected ], but found } instead. [[<[([]))<([[{}[[()]]] - Expected ], but found )
instead. [{[{({}]{}}([{[{{{}}([] - Expected ), but found ] instead. [<(<(<(<{}))><([]([]() - Expected >, but found )
instead. <{([([[(<>()){}]>(<<{{ - Expected ], but found > instead. Stop at the first incorrect closing character on each
corrupted line.

To get the right path calculate the syntax error score for a line, take the first illegal character on the line and look
it up in the following table:

- ): 16 points.
- ]: 64 points.
- }: 1080 points.
- : 22222 points.

In the above example, an illegal ) was found twice (2\*16 = 32 points), an illegal ] was found once (64 points), an
illegal } was found once (1080 points), and an illegal > was found once (22222 points). So, the total syntax error score
for this file is 32 + 64 + 1080 + 22222 = 23398.

Question
Find the first illegal character in each corrupted line of the navigation subsystem. What is the total syntax error
score for those errors?

### Solution

To solve this problem, we will process each line of the navigation subsystem to identify and analyze the first illegal character in corrupted lines.

Identify Pairs of Matching Characters:

- ( must close with ).
- [ must close with ].
- { must close with }.
- < must close with >.

Detect Corrupted Lines:

- Use a stack to validate the chunks in a line.
- Push each opening character ((, [, {, <) onto the stack.
- When a closing character is encountered, check if it matches the character at the top of the stack.
- If it matches, pop the top of the stack.
- If it doesn’t match, the line is corrupted, and the first illegal character is the one encountered.
- Calculate Syntax Error Score:

For each corrupted line, get the score of the illegal character based on:

- ) = 16 points
- ] = 64 points
- } = 1080 points

= 22222 points
Sum the scores of all corrupted lines.

Ignore Incomplete Lines:
Lines where the stack is not empty at the end of processing but have no illegal characters are incomplete and should be ignored.
