# wc.py
import sys

if len(sys.argv) != 2:
    print("Usage: python wc.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

with open(filename, "r") as file:
    text = file.read()
    lines = text.count("\n")
    characters = len(text)

print(f"Lines: {lines}")
print(f"Characters: {characters}")