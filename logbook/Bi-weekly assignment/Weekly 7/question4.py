message = input("Enter the encrypted message: ")

# Dictionary to store frequency of letters
frequency = {}

# Initialize counts for all letters a–z to 0
for letter in "abcdefghijklmnopqrstuvwxyz":
    frequency[letter] = 0

# Count letters (case-insensitive)
for char in message.lower():
    if char.isalpha():
        frequency[char] += 1

# Sort letters by frequency (highest first)
sorted_letters = sorted(frequency.items(), key=lambda item: item[1], reverse=True)

# Display the six most common letters
print("\nSix most common letters:")
for letter, count in sorted_letters[:6]:
    print(f"{letter} : {count}")