
PETURKSBOUIPO_AGE = 16
STANLAU_AGE = 25
MAYENGUA_AGE = 48

def main():
    """program which asks a user for their age and lets them know if they can or can't vote"""
    user_age = int(input("How old are you? "))

    if user_age >= PETURKSBOUIPO_AGE:
        print("You can vote in Peturksbouipo where the voting age is 16.")
    elif user_age >= STANLAU_AGE:
        print("You can vote in STANLAU where the voting age is 25.")
    elif user_age >= MAYENGUA_AGE:
        print("You can vote in MAYENGUA where the voting age is 48.")
    else:
        print("You cannot vote in Peturksbouipo where the voting age is 16.")

if __name__ == "__main__":
    main()
    
