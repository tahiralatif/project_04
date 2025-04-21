MAX_LENGTH = 4  

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()  
        print("Removed:", removed_item)

def get_lst():
    lst = []
    elem = input("Enter element (or press enter to stop): ")
    while elem != "":
        lst.append(elem)
        elem = input("Enter element (or press enter to stop): ")
    return lst

def main():
    lst = get_lst()
    print("Original list:", lst)
    shorten(l st)
    print("Final list:", lst)

if __name__ == "__main__":
    main()
