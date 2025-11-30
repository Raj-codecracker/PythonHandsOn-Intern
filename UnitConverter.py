def kg_to_gram():
    kg = float(input("Enter value in kilograms: "))
    grams = kg * 1000
    print(f"{kg} kg = {grams} grams")


def kg_to_milligram():
    kg = float(input("Enter value in kilograms: "))
    milligrams = kg * 1_000_000
    print(f"{kg} kg = {milligrams} milligrams")


def celsius_to_fahrenheit():
    c = float(input("Enter temperature in Celsius: "))
    f = (c * 9/5) + 32
    print(f"{c}°C = {f}°F")


def fahrenheit_to_celsius():
    f = float(input("Enter temperature in Fahrenheit: "))
    c = (f - 32) * 5/9
    print(f"{f}°F = {c}°C")


def celsius_to_kelvin():
    c = float(input("Enter temperature in Celsius: "))
    k = c + 273.15
    print(f"{c}°C = {k} K")


def kelvin_to_celsius():
    k = float(input("Enter temperature in Kelvin: "))
    c = k - 273.15
    print(f"{k} K = {c}°C")


def main():
    while True:
        print("\n========== UNIT CONVERTER ==========")
        print("1. Kilogram to Gram")
        print("2. Kilogram to Milligram")
        print("3. Celsius to Fahrenheit")
        print("4. Fahrenheit to Celsius")
        print("5. Celsius to Kelvin")
        print("6. Kelvin to Celsius")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == "1":
            kg_to_gram()
        elif choice == "2":
            kg_to_milligram()
        elif choice == "3":
            celsius_to_fahrenheit()
        elif choice == "4":
            fahrenheit_to_celsius()
        elif choice == "5":
            celsius_to_kelvin()
        elif choice == "6":
            kelvin_to_celsius()
        elif choice == "7":
            print("Thank you for using the Unit Converter!")
            break
        else:
            print("Invalid option. Try again.")

main()
