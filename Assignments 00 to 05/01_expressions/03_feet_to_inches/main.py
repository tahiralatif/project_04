# 03_feet_to_inches.
 # This code is a simple feet to inches converter.
    # It takes input in feet and converts it to inches.


def feet_to_inches():
    try:
        """ Convert feet to inches"""
        feet: float = float(input("Enter feet: "))
        inches = feet * 12
        print(f"{feet} feet is equal to {inches} inches.")
        
    except ValueError:
        print("Invalid input. Please enter a number.")



def main():
    """Main function"""
    print(" Welcome to the feet 🐾 to inches converter!")
    feet_to_inches()
if __name__ == "__main__":
    main()
   