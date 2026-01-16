# spell.py
import sys

if len(sys.argv) != 3:
    print("Usage: python spell.py <textfile> <dictionary>")
    sys.exit(1)

textfile = sys.argv[1]
dictionary_file = sys.argv[2]

with open(dictionary_file, "r") as d:
    dictionary = set(word.strip().lower() for word in d)

with open(textfile, "r") as t:
    words = t.read().lower().split()

misspelled = set()

for word in words:
    word = word.strip(".,!?;:\"'()")
    if word and word not in dictionary:
        misspelled.add(word)

for word in sorted(misspelled):
    print(word)