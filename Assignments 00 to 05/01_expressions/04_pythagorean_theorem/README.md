# Pythagorean Theorem Calculator

## Overview
This Python program calculates the hypotenuse of a right triangle using the **Pythagorean Theorem**:

\[ c^2 = a^2 + b^2 \]

Where:
- `a` and `b` are the two perpendicular sides.
- `c` is the hypotenuse (longest side opposite the right angle).

The program takes user input for the two shorter sides and computes the hypotenuse.

---
## How It Works
1. The user is prompted to enter the lengths of the two perpendicular sides.
2. The program calculates the hypotenuse using the formula:
   ```python
   hypotenuse = math.sqrt(side1 ** 2 + side2 ** 2)
   ```
3. The result is displayed with two decimal places.

---
## Code Explanation
```python
import math

def get_hypotenuse():
    """Calculate the Length of the Hypotenuse"""
    side1 = float(input("Enter the length of the first side: "))
    side2 = float(input("Enter the length of the second side: "))
    hypotenuse = math.sqrt(side1 ** 2 + side2 ** 2)
    print(f"The Length of the Hypotenuse is: {hypotenuse:.2f}")

def main():
    """Main function to run the Pythagorean theorem calculation"""
    print("\nWelcome to the Pythagorean Theorem Calculator!\n")
    get_hypotenuse()

if __name__ == "__main__":
    main()
```

---
## Example Usage
### Input:
```
Enter the length of the first side: 3
Enter the length of the second side: 4
```
### Output:
```
The Length of the Hypotenuse is: 5.00
```

---
## Right Triangle Diagram
Below is a visual representation of a right triangle:

```
       /|
      / |
  c  /  | b
    /___|
      a
```
Where:
- **a** = first side
- **b** = second side
- **c** = hypotenuse (calculated by the program)

---
## Requirements
- Python 3.x
- `math` module (built-in)

---
## How to Run
1. Copy and paste the code into a Python file (`pythagorean.py`).
2. Run the file using the command:
   ```sh
   python pythagorean.py
   ```
3. Follow the prompts and enter the side lengths.
4. The program will display the hypotenuse.

---
## License
This project is free to use and modify.

Happy Coding! 🚀

