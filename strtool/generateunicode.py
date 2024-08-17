"""Module for generating unicode string
ChatGPT, `Characters commonly used in Western PCs`
2024-07-29
"""


import unicodedata
import string

# Define ranges for various Unicode blocks
unicode_ranges = [
    (0x0020, 0x007F),  # Basic Latin
    (0x00A0, 0x00FF),  # Latin-1 Supplement
    (0x0100, 0x017F),  # Latin Extended-A
    (0x0180, 0x024F),  # Latin Extended-B
    (0x1E00, 0x1EFF),  # Latin Extended Additional
    (0x0370, 0x03FF),  # Greek and Coptic
    (0x0400, 0x04FF),  # Cyrillic
    (0x0500, 0x052F),  # Cyrillic Supplement
]

# Function to get all characters in the specified ranges
def get_characters_from_ranges(ranges):
    characters = ""
    for start, end in ranges:
        for codepoint in range(start, end + 1):
            characters += chr(codepoint)
    return characters

# Get all characters from the defined Unicode ranges
european_characters = get_characters_from_ranges(unicode_ranges)

# Optionally, filter out non-printable characters
printable_characters = ''.join(
    c for c in european_characters if unicodedata.category(c)[0] != 'C'
)

# Print the string (or process it further)
print(printable_characters)

# Length of the resulting string
print("Number of characters:", len(printable_characters))

print(string.printable)
