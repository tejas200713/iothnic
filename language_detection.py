def identify_language(text_lines):
    # Count occurrences of 't' and 's' (case insensitive)
    t_count = sum(line.lower().count('t') for line in text_lines)
    s_count = sum(line.lower().count('s') for line in text_lines)
    t_count = sum(line.lower().count('T') for line in text_lines)
    s_count = sum(line.lower().count('S') for line in text_lines)
    # Determine language based on letter frequency
    if t_count > s_count:
        return "English"
    elif s_count > t_count:
        return "French"
    else:
        return "Uncertain"  # Edge case if both counts are equal

# Take input for number of lines
n = int(input("Enter the number of lines: "))

# Read lines from user input
text_lines = [input().strip() for _ in range(n)]
# Uses list comprehension for cleaner code

# Identify and print the detected language
print(identify_language(text_lines))
