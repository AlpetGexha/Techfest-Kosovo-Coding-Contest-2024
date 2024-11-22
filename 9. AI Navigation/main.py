input = open("input.txt", "r").read()

lines = input.split("\n")

# Points for illegal characters
error_points = {
    ')': 16,
    ']': 64,
    '}': 1080,
    '>': 22222,
}

# Matching pairs
opening_chars = "([{<"
closing_chars = ")]}>"
matching_pairs = dict(zip(closing_chars, opening_chars))

# Function to calculate syntax error score
def calculate_syntax_error_score(lines):
    total_score = 0

    for line in lines:
        stack = []
        for char in line:
            if char in opening_chars:
                stack.append(char)
            elif char in closing_chars:
                if stack and stack[-1] == matching_pairs[char]:
                    stack.pop()
                else:
                    # Corrupted line, add points for the first illegal character
                    total_score += error_points[char]
                    break  # Stop processing this line

    return total_score

total_score = calculate_syntax_error_score(lines)
print(total_score)
#23398
