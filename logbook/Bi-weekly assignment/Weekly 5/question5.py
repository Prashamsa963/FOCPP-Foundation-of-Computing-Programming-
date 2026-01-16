import sys

args = sys.argv[1:]

if not args:
    print("No temperatures provided")
    sys.exit()

temps = []

for temp in args:
    temps.append(float(temp[:-1]))  # remove 'C'

print("Maximum:", max(temps))
print("Minimum:", min(temps))
print("Mean:", sum(temps) / len(temps))