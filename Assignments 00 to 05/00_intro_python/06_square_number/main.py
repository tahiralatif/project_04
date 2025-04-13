# square numbers

def main():
    """This program calculates the square of a number."""
    print("\nWelcome to the Square Number Program!\n")
    num : float = float(input("Enter a Number to see its square: "))
    square : float = num ** 2
    print(f"The square of {num} is {square}")
    print("Thank you for using the square number program!")
if __name__ == "__main__":
    main()