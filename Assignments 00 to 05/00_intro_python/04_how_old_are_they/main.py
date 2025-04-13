# Anton is 21 years old. 
# Beth is 6 years older than Anton. 
# Chen is 20 years older than Beth. 
# Drew is as old as Chen plus Anton's age. 
# Ethan is as old as Chen.

Anton = 21
Beth = Anton + 6
Chen = Beth + 20
Drew = Chen + Anton
Ethan = Chen



def main():
    """ the program calculates the ages of Anton, Beth, Chen, Drew and Ethan """

    Anton = 21
    Beth = Anton + 6
    Chen = Beth + 20    
    Drew = Chen + Anton
    Ethan = Chen


    ages = {
        "anton" : Anton,
        "beth": Beth,
        "chen": Chen,
        "drew": Drew,
        "ethan": Ethan

    }

    user_input = input("Enter the name of the person you want to know the age of \n(Anton, Beth, Chen, Drew, Ethan): ").strip().lower()
    
    if user_input in ages:
        print(f"{user_input.capitalize()}'s age is {ages[user_input]} years old.")
    else:
        print("Sorry, I don't know that person.")

if __name__ == "__main__":
    main()

