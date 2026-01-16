# grep.py
import sys

if len(sys.argv) != 3:
    print("Usage: python grep.py <pattern> <filename>")
    sys.exit(1)

pattern = sys.argv[1]
filename = sys.argv[2]

with open(filename, "r") as file:
    for line in file:
        if pattern in line:
            print(line.rstrip())