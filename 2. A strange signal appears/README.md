### Level 2:

## A strange signal appears

Something strange is happening with Toma’s communication system. His handheld cyberdeck, essential for receiving mission
directives, is suddenly intercepting encrypted signals that defy all logic. It feels like someone—or something—is
broadcasting secret messages through the city’s grid.

After a quick inspection, you realize these signals are encoded using an unfamiliar system. Toma’s device lacks the
power to decrypt them, so you pull out your portable rig to develop an emulator for the encoding algorithm.

The messages were transmitted using the BYTE Interchange Transmission System (BITS)—a cutting-edge method for
compressing complex numeric data into a binary sequence. Your rig managed to save the intercepted transmission in
hexadecimal format (your puzzle input).

The first step to decode the message is to convert the hexadecimal data into binary. Each hexadecimal character
translates directly into four bits of binary data:

```
0 = 0000
1 = 0001
2 = 0010
3 = 0011
4 = 0100
5 = 0101
6 = 0110
7 = 0111
8 = 1000
9 = 1001
A = 1010
B = 1011
C = 1100
D = 1101
E = 1110
F = 1111
```

To transcode the BITS transmission, which is a super old unsecured protocol, you only need to transfer the number into
binary format and multiply the sum of ones by the sum of zeros (that are not padded on the left of the number) to get
the key.

### Example:

If the message is 12, the binary format is 0001 (1 without the zeros padding in front) and 0010 (10 without the zeros
padding in the front) and the key is 2\*1 = 2.

### Question

What is the key for the BITS transmission? Time to decode the chaos and find out what the message is about.

## Solution

Steps to Decode the BITS Transmission
Convert Hexadecimal to Binary: Each hexadecimal character converts to four binary bits using the provided mappings.

Count Ones and Non-Padded Zeros:

Identify all 1s in the binary representation and sum them.
Identify all 0s that are part of the actual data (not left-padded) and sum them.

Calculate the Key: Multiply the sum of 1s by the sum of non-padded 0s to get the key.
