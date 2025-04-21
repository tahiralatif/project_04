# Function to add 3 copies of data to the list
def add_three_copies(my_list, data):
    for i in range(3):           # Loop 3 times
        my_list.append(data)     

# Main function
def main():
    message = input("Enter a message to copy: ")  # Take user input
    my_list = []  
    print("List before:", my_list)  
    add_three_copies(my_list, message)  
    print("List after:", my_list) 

# Ensure the main function is called
if __name__ == "__main__":
    main()
