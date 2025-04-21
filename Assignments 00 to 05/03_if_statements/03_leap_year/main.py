# leap  year

def main():
    """program to check if a year is a leap year or not"""
    try:
        year = int(input("Please input a year: "))

        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    print(f"{year} is a leap year")
                else:
                    print(f"{year} is not a leap year")
            else:
                print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    except ValueError:
        print("Please enter a valid year")
if __name__ == "__main__":
    main()                


    