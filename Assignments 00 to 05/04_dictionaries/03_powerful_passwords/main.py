from hashlib import sha256

# Step 1: Hashing function
def hash_password(password):
    return sha256(password.encode()).hexdigest()

def register(users):
    email = input("Enter your email to register: ")
    password = input("Enter your password: ")
    users[email] = hash_password(password)
    print(f"User {email} ✅ registered successfully!")

def login(users):
    email = input("Enter your email to login: ")
    password = input("Enter your password: ")
    if email in users and users[email] == hash_password(password):
        print(f"User {email} ✅ logged in successfully!")
    else:
        print("Invalid email or password ❌")

def main():
    users = {}
    while True:
        print("\n 1. Register")
        print(" 2. Login")
        print(" 3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            register(users)
        elif choice == '2':
            login(users)
        elif choice == '3':
            print("👋 Exiting... Bye!")
            break
        else:
            print("⚠️ Invalid option. Try again.")  
if __name__ == '__main__':
    main()          