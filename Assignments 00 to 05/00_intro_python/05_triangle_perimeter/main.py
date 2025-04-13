# 05_triangle_perimeter

def main():
    """Get The User Input And Calculate The Perimeter Of The Triangle."""
    side1: float = float(input("Enter the length of the first side: "))
    side2: float = float(input("Enter the length of the second side: "))
    side3: float = float(input("Enter the length of the third side: "))

    perimeter = side1 + side2 + side3
    print(f"{side1} + {side2} + {side3} = {perimeter}")
    print(f"The perimeter of the triangle is {perimeter}")

if __name__ == "__main__":
    main()
else:
    print("This module is not meant to be run directly.")
