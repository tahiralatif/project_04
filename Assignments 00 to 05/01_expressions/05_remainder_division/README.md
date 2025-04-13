
# Remainder Division Program

This Python program calculates the **quotient** and **remainder** of two integers using **integer division** and the **modulo operator**.

## 📌 Features

- Takes input from the user for two integers: `dividend` and `divisor`.
- Calculates:
  - **Quotient** using `//` operator (integer division)
  - **Remainder** using `%` operator (modulo)
- Handles errors such as:
  - Division by zero
  - Invalid (non-integer) inputs

## 📐 Formula Used

```
Quotient = Dividend // Divisor
Remainder = Dividend % Divisor
```

For example:
```
Dividend = 17
Divisor  = 5

Quotient = 17 // 5 = 3
Remainder = 17 % 5 = 2
```

So, `17 = 5 * 3 + 2`

## 🧠 What You Learn

- Basic arithmetic operations in Python
- Exception handling using `try`, `except`
- How integer division and modulo work

## ▶️ How to Run

Make sure Python is installed, then run the script using:

```bash
python remainder_division.py
```

## 🧾 Sample Output

```
Welcome to the Remainder Division Program!

This program calculates the quotient and remainder of two integers.
Enter the dividant: 17
Enter the dividor: 5
The quotient is: 3 and the remainder is: 2
```

## 📎 Note

- If you enter `0` as the divisor, the program will alert you that division by zero is not allowed.
- You must input only valid integers.
