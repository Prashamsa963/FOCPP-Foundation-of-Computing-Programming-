# Dictionary to store countries and their capitals
countries = {}

print("Country–Capital Manager")
print("Type 'exit' to stop the program.\n")

while True:
    country = input("Enter the name of a country: ").strip()

    # Exit condition
    if country.lower() == "exit":
        print("\nProgram terminated.")
        break

    # Normalize country name (case-insensitive handling)
    country_key = country.lower()

    if country_key in countries:
        print(f"The capital of {country.title()} is {countries[country_key]}.\n")
    else:
        capital = input(f"I don't know the capital of {country.title()}. Please enter it: ").strip()
        countries[country_key] = capital
        print(f"Saved! The capital of {country.title()} is now stored as {capital}.\n")