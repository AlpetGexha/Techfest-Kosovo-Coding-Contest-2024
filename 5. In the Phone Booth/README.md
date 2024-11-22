### Level 5

## In the Phone Booth

You arrive at the location that was transmitted and stumble upon a glowing terminal—an old information kiosk hidden in a
phone booth. It promises access to a list of secure zones (?), but the data feed is encrypted and riddled with decoy
entries. Fortunately, nearby scrawled instructions scraped into the booths aluminium hint at how to decode the real
zones from the noise. First step: filter out the decoy data.

Each secure zone entry consists of:

- An encrypted name (lowercase letters separated by dashes)
- Followed by a dash, a sector ID, and a checksum in square brackets.

A secure zone is real (not a decoy) if the checksum is made up of the five most common letters in the encrypted name,
listed in order of frequency, with ties broken alphabetically.

### Example:

- aaaaa-bbb-z-y-x-123[abxyz]: Real. The most common letters are a (5), b (3), z, y, and x (1 each).
- a-b-c-d-e-f-g-h-987[abcde]: Real. The most common letters are a, b, c, d, and e (1 each, alphabetically ordered).
- not-a-real-room-404[oarel]: Real. The most common letters are o, a, r, e, and l.
- totally-fake-room-200[decoy]: Decoy. The checksum does not match the most common letters.

Your task is to decrypt the list, identify the real zones, and determine which ones you can use. Time to decode the
chaos of the undercity and find your way forward.

### Question

What is the sum of the sector IDs of the real rooms?

### Sloution

To solve this problem, we need to determine which zones (entries) are "real" based on the checksum validation rules and then compute the sum of their sector IDs.

Steps:

- Input Parsing: Each zone entry is in the format:

```
name-sectorID[checksum]
```

- name consists of lowercase letters separated by dashes (-).
- sectorID is a number.
- checksum is in square brackets ([]).

Validation:

- Count the frequency of each letter in the name (ignoring dashes -).
- Sort the letters first by frequency (descending) and then alphabetically.
- Check if the first five letters in this sorted order match the checksum.

Summing Sector IDs:

- If the entry is real, add its sectorID to the total.
