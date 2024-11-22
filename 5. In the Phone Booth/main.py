from collections import Counter

input = open("input.txt", "r").read()

def is_real_room(name, checksum):
    # Count frequency of each letter (ignoring dashes)
    letter_counts = Counter(name.replace('-', ''))
    # print(letter_counts)
    # Sort by frequency (descending) and alphabetically
    sorted_letters = sorted(letter_counts.items(), key=lambda x: (-x[1], x[0]))
    # print(sorted_letters)
    # Extract the top 5 letters for checksum comparison
    calculated_checksum = ''.join(letter for letter, _ in sorted_letters[:5])
    # print(calculated_checksum)
    # print(checksum)

    return calculated_checksum == checksum


def sum_of_real_rooms(entries):
    total_sector_id = 0

    for entry in entries:
        # Parse the entry (format: name-sectorID[checksum])
        parts = entry.rsplit('-', 1)
        name = parts[0]
        sector_id, checksum = parts[1].split('[')
        sector_id = int(sector_id)
        checksum = checksum.strip(']')

        # Check if the room is real and add its sector ID if so
        if is_real_room(name, checksum):
            total_sector_id += sector_id

    return total_sector_id


entries = input.split('\n')
result = sum_of_real_rooms(entries)
print(result)
