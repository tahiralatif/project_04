# continuously asks the user to enter values

def main():
    lst = []
    val = input("Enter a value (or 'done' to finish): ")
    while val.lower() != 'done':
        try:
            # Convert the input to an integer and append it to the list
            lst.append((val))
            val = input("Enter a value (or 'done' to finish): ")
        except ValueError:
            print("Invalid input. Please enter a number or 'done' to finish.")
            val = input("Enter a value (or 'done' to finish): ")
    print("You entered:", lst)
if __name__ == "__main__":
    main()            