def length_converter():
    print("\nLength Conversion: (1) Meters to Feet (2) Feet to Meters")
    choice = input("Choose conversion (1/2): ")
    value = float(input("Enter value: "))
    if choice == '1':
        print(f"{value} meters = {value * 3.28084:.2f} feet")
    elif choice == '2':
        print(f"{value} feet = {value / 3.28084:.2f} meters")
    else:
        print("Invalid choice")

def weight_converter():
    print("\nWeight Conversion: (1) Kilograms to Pounds (2) Pounds to Kilograms")
    choice = input("Choose conversion (1/2): ")
    value = float(input("Enter value: "))
    if choice == '1':
        print(f"{value} kg = {value * 2.20462:.2f} lb")
    elif choice == '2':
        print(f"{value} lb = {value / 2.20462:.2f} kg")
    else:
        print("Invalid choice")

def temperature_converter():
    print("\nTemperature Conversion: (1) Celsius to Fahrenheit (2) Fahrenheit to Celsius")
    choice = input("Choose conversion (1/2): ")
    value = float(input("Enter temperature: "))
    if choice == '1':
        print(f"{value}°C = {value * 9/5 + 32:.2f}°F")
    elif choice == '2':
        print(f"{value}°F = {(value - 32) * 5/9:.2f}°C")
    else:
        print("Invalid choice")

def main():
    while True:
        print("\n--- Unit Converter ---")
        print("1. Length")
        print("2. Weight")
        print("3. Temperature")
        print("4. Exit")
        option = input("Choose a category (1-4): ")

        if option == '1':
            length_converter()
        elif option == '2':
            weight_converter()
        elif option == '3':
            temperature_converter()
        elif option == '4':
            print("Exiting the converter. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
