
# Mass-Energy Equivalence Calculator

## Description

This Python program calculates the energy equivalent of a given mass using **Einstein's mass-energy equivalence formula**:

\[ E = m 	imes c^2 \]

Where:
- \( E \) is the energy in joules (J)
- \( m \) is the mass in kilograms (kg)
- \( c \) is the speed of light in a vacuum, which is \( 299,792,458 \, 	ext{m/s} \)

The program asks the user to input the mass (in kilograms) and then calculates the energy (in joules) using the formula. It also includes **error handling** to ensure that the user enters a valid numeric input.

## Features

- Asks the user for the mass in kilograms.
- Calculates the energy using Einstein's formula \( E = m 	imes c^2 \).
- Handles invalid user input gracefully with error handling.
- Outputs the result in a clear format.

## Installation

There is no installation needed. Just make sure you have Python 3.x installed.

## Usage

1. Run the script.
2. Enter the mass in kilograms when prompted.
3. The program will display the energy equivalent of the entered mass.

Example output:
```bash
Enter mass in kg: 100
Using Einstein's formula: E = m * C^2
Mass: 100.0 kg = 8.987551787368176e+18 joules
```

## Error Handling

If the user inputs a non-numeric value, the program will prompt them to enter a valid numeric value for the mass.

Example of invalid input:
```bash
Enter mass in kg: abc
Invalid input. Please enter a numeric value for mass.
```

## Code

```python
C: int = 299792458  # Speed of light in vacuum (m/s)

def main():
    try:
        mass_in_kg: float = float(input("Enter mass in kg: "))
        energy_in_joules: float = mass_in_kg * (C ** 2)
        
        # Display results after calculation
        print(f"
Using Einstein's formula: E = m * C^2")
        print(f"Mass: {mass_in_kg} kg = {energy_in_joules} joules")
    
    except ValueError:
        print("Invalid input. Please enter a numeric value for mass.")

if __name__ == "__main__":
    main()
```

## License

This project is open-source and free to use.
