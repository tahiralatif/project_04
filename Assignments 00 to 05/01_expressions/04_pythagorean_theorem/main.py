# 04_pythagorean_theorem
import math

def get_hypotenius():
    """Calculate the Lenght of Hypotenuse"""

    side1 : float = float(input("Enter the length of the first side: "))
    side2 : float = float(input("Enter the length of the second side: "))
    hypotenuse : float = math.sqrt(side1 ** 2 +  side2 ** 2) 
    print(f"The Length of the Hypotenuse is: {hypotenuse:.2f}")

def main():
    """Main function to run the Pythagorean theorem calculation"""
    print("\nWelcome to the Pythagorean Theorem Calculator!\n")
    get_hypotenius()
if __name__ == "__main__":
    main()
