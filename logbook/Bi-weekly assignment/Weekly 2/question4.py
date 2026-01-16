# Sweet distribution program

sweets = int(input("How many sweets are there? "))
pupils = int(input("How many pupils are present? "))

each = sweets // pupils
leftover = sweets % pupils

print("Each pupil will receive", each, "sweets.")
print("There will be", leftover, "sweets left over.")
