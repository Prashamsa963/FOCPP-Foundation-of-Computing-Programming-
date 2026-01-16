def count_letters(text):
    upper = 0
    lower = 0

    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1

    return upper, lower

# Test program
s = input("Enter a string: ")
upper, lower = count_letters(s)
print("Uppercase:", upper)
print("Lowercase:", lower)