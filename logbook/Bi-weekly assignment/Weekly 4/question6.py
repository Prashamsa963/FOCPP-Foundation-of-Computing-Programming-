temp = input("Enter temperature (e.g. 25C): ")

value = float(temp[:-1])
result = (value * 9/5) + 32

print(f"{result}F")