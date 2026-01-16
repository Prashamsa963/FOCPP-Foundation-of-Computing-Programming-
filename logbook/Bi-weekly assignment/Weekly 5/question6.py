import sys
import shutil

if len(sys.argv) < 2:
    print("Please provide a file name")
    sys.exit()

original = sys.argv[1]
backup = original + ".backup"

try:
    shutil.copyfile(original, backup)
    print("Backup created:", backup)
except:
    print("File not found or error occurred")