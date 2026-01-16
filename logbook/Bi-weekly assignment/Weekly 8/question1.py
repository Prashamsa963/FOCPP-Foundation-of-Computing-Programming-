# nl.py
import sys

if len(sys.argv) != 2:
    print("Usage: python nl.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

with open(filename, "r") as file:
    for i, line in enumerate(file, start=1):
        print(f"{i}\t{line.rstrip()}")