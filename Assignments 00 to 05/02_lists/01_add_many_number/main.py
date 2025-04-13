# add_many_number

def many_numbers(numbers) -> int:
    """
    This function takes any number of arguments and returns their sum.
    
    :param args: Numbers to be summed
    :return: Sum of the numbers
    """
    total = 0
    for number in numbers:
        total += number
    return total
def main():
    """main function to test the many_numbers function"""    
    number: list[int] = [1, 2, 3, 4, 5]
    result = many_numbers(number)
    print(f"\nThe sum of {number} is {result}.\n")
if __name__ == "__main__":
    main()         