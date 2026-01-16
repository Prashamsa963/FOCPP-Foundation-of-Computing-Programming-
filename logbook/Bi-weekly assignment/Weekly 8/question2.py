# diff.py
import sys

if len(sys.argv) != 3:
    print("Usage: python diff.py <file1> <file2>")
    sys.exit(1)

file1, file2 = sys.argv[1], sys.argv[2]

with open(file1, "r") as f1, open(file2, "r") as f2:
    if f1.read() == f2.read():
        print("The files are the same.")
    else:
        print("The files are different.")