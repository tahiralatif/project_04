# Favorite Animal Program

## Description
This is a simple Python program that asks the user for their favorite animal and ensures they enter a valid string (not a number). If the user enters a number, they are prompted again until a valid animal name is provided.

## Features
- Prompts the user to enter their favorite animal.
- Ensures the input is a valid string and not a number.
- Displays the favorite animal after successful input.
- Uses a loop to handle invalid inputs.

## How to Run
1. Make sure you have Python installed.
2. Save the script as `favorite_animal.py`.
3. Open a terminal or command prompt.
4. Run the script using the command:
   ```sh
   python favorite_animal.py
   ```

## Code Explanation
- The program prints a welcome message.
- A `while True` loop ensures that the input is validated.
- If the user enters a number, an error message is displayed, and they must enter a valid animal name.
- Once a valid input is received, the program prints the chosen animal and exits.

## Example Output
```
Program What's your favorite animal?
------------------------------------
This program asks the user what their favorite animal is.

What's Your Favourite Animal? 123
Invalid! Please Enter Animal Name not a Number
What's Your Favourite Animal? Cat
My Favourite Animal is also Cat!
```

## Author
- Developed by ##Tahira Latif