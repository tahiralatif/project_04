#  Fahrenheit to Celsius

def main():
    try:
        fahrenheit: float = float(input("\nEnter a value in Fahrenheit to converts Celcius: "))
        celcius = (fahrenheit - 32) * 5 / 9
        print(f"\nFahrenheit to Celcius: {fahrenheit} Fahrenheit = {celcius} Celcius")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
if __name__ == "__main__":
    main()



