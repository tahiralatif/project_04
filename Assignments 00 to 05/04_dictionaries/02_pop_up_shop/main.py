def main():
    fruits = {'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}
    
    total_cost = 0

    while True:
        user_input = input("What fruit do you want to buy? (press Enter to finish): ").lower()
        
        if user_input == '':
            break
        elif user_input not in fruits:
            print("Sorry, we don't have that fruit.")
            continue

        price = fruits[user_input]
        amount_bought = int(input(f"How many ({user_input}) do you want to buy?: "))
        fruit_total = price * amount_bought
        total_cost += fruit_total

        print(f"{user_input.capitalize()} {price} x {amount_bought} = ${fruit_total:.2f}")
    
    print(f"\nYour Total Cost: ${total_cost:.2f}")
    print("Thank you for shopping with us!")
if __name__ == "__main__":
    main()