import re

description = "the quick brown fox"

patterns = [r"Brown (\w+)",
            r"bRown (\w+)",
            r"brown (\w+)"]

for pattern in patterns:
    match = re.search(pattern, description, re.IGNORECASE)
    if match:
        print(f"{match} exist in the sentence")