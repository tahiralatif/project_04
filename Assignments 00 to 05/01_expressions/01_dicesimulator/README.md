# Dice Simulator

## Description
This Python program simulates rolling two six-sided dice three times. It prints the results of each roll, showing the values of both dice and their sum. The purpose of this program is to demonstrate variable scope in Python.

## Features
- Uses the `random` module to generate dice rolls.
- Simulates rolling two dice and calculates their total.
- Uses a loop to roll the dice three times efficiently.
- Demonstrates proper Python coding conventions and best practices.

## How to Run the Program
1. Ensure you have Python installed (Python 3.x recommended).
2. Save the script as `dicesimulator.py`.
3. Open a terminal or command prompt and navigate to the script’s directory.
4. Run the script using:
   ```sh
   python dicesimulator.py
   ```
5. The program will output three sets of dice rolls with their sums.

## Code Explanation
### `roll_dice()`
This function generates two random numbers (1-6) and prints their sum.

### `main()`
Calls `roll_dice()` three times using a loop for efficiency.

### `if __name__ == "__main__":`
Ensures that the script runs only when executed directly.

## Example Output
```
Rolling dice three times:
Die1 3 + Die2 5 = Total of two dice 8
Die1 2 + Die2 6 = Total of two dice 8
Die1 4 + Die2 1 = Total of two dice 5
```

## Improvements
- You can modify `num_sides` to simulate different dice (e.g., 8-sided or 20-sided dice).
- You can allow user input for the number of rolls instead of rolling exactly three times.

## Author
Developed by [Your Name]

