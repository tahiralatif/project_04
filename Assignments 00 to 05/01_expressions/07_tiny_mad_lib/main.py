def main():
    print("Welcome to the Mad Libs game!")
    print("In this game, you will be asked to provide some words, and then we will create a funny story using those words.\n")
    
    try:
        # Prompts for user input
        prompts = [
            ("adjective", "Please type an adjective (e.g., happy, unhappy, excited, nervous, sad, scared): "),
            ("verb", "Please type a verb (e.g., run, jump, fly, eat, dance): "),
            ("noun", "Please type a noun (e.g., dog, car, teacher, mountain, idea): "),
            ("noun2", "Please type another noun (e.g., your name, your favourite person, animal): "),
            ("place", "Please type a place (e.g., park, school, beach, city): "),
            ("country", "Please type a country (e.g., USA, Canada, France, Japan): "),
            ("color", "Please type a color (e.g., red, blue, green, yellow): "),
            ("transport", "Please type a mode of transport (e.g., car, bus, train, bicycle): ")
        ]

        inputs = {}

        # Loop through prompts and gather user input
        for prompt, example in prompts:
            inputs[prompt] = input(f"{example}\n")

        # Create the story
        story = f"""
        Once upon a time, {inputs['noun']} went to {inputs['country']} with {inputs['noun2']} in a {inputs['transport']}.
        They were so {inputs['adjective']} and wore {inputs['color']} clothes. After reaching {inputs['country']}, 
        they went for a picnic at {inputs['place']} and enjoyed {inputs['verb']} together.
        """

        # Print the final story
        print("\nHere is your Mad Libs story:\n")
        print(story)

    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()
