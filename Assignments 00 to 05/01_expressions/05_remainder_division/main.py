# remainder_division

def remainder_division():
    try:
        dividant : int = int(input("Enter the dividant: ")) 
        dividor: int = int(input("Enter the dividor: ")) 
        quotient :int = dividant // dividor
        remainder :int = dividant % dividor
        print(f"The quotient is: {quotient} and the remainder is: {remainder}")   
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Invalid input. Please enter valid integers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}") 
def main():
    """
    Main function to execute the remainder division program.
    """
    print("\nWelcome to the Remainder Division Program!\n")
    print("\nThis program calculates the quotient and remainder of two integers.")
    remainder_division()
if __name__ == "__main__":
    main()          

