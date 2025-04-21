
def get_first_element(lst):
    """
    Prints the first element of a provided list.
    """

    print(lst[0])



def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem: str = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

def main():
    lst = get_lst()
    print(f"\nThe list is: {lst}\n")
    if len(lst) == 0:
        print("The list is empty.")
    else:
        print("The first element of the list is:")
    get_first_element(lst)


if __name__ == '__main__':
    main()

