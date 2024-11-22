# read the input.txt file
import mmh3

input = open("input.txt", "r").read()


# Loot data (trimmed to relevant section for hashing)
loot_data = (
   input
)

# Generate MurmurHash3 128-bit hash (x86)
hash_result = mmh3.hash128(loot_data, seed=0, x86=True)
print(hash_result)


