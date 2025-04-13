def main():
    print("""
Program What's your favorite animal? 
# ------------------------------------
# This program asks the user what their favorite animal is.
""")
    while True:
        try:
            fav_animal: str = input("What's Your Favourite Animal? ")
            if fav_animal.isdigit():
                print("Invalid! Please Enter Animal Name not a Number")
            else:
                break  # Valid input milne par loop exit kar do
        except ValueError:
            print("Please Enter a Valid string")

    print(f"My Favourite Animal is also {fav_animal}!")

if __name__ == "__main__":
    main()
