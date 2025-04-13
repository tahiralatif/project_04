

def main():

    print(
    """ Program That Sum Two Number
    ---------------------------------
    User Add Two Integer And prints Their Sum
    """
    )

    while True:
        try:
            num1: int =  int(input("Enter your First Number: "))
            num2 :int = int(input("Enter Your Second Number: "))
            break
        except ValueError:
            print("Invalid Input! Please ennter the integers only \n")

    sum = num1 + num2
    print(f"The Total is {num1} + {num2} = {sum}")

    

if __name__ == "__main__":
    main()

   