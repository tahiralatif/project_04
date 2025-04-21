# print 20 even numbers starting from 0

def main():
    """ Print 20 even numbers starting from 0 """
    print("The program will print first 20 even numbers starting from 0")

def even_numbers():
    """ Function to print even numbers """
    count = 0  # Initialize count
    num = 0    # Initialize number

    while count < 20:
        if num % 2 == 0:
            print(num)
            count += 1
        num += 1

if __name__ == "__main__":
    main()
    even_numbers()
