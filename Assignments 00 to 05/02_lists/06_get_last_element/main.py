# get last element of a list

def get_last_element(lst):
    if lst:
        print(lst[-1])
    else:
        print("The list is empty.")  

def get_lst():
    lst = [] 
    elem = input("Enter element (or 'press' enter to finish): ")
    while elem != "":
        lst.append(elem)
        elem = input("Enter element (or 'press' enter to finish): ")
    return lst
def main():
    lst = get_lst()
    print(f"Your list is: {lst}")
    print("The last element of the list is: ", end="")
    get_last_element(lst)
    
if __name__ == "__main__":
       main()    
    