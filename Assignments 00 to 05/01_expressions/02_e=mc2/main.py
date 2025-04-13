C: int = 299792458  # Speed of light in vacuum (m/s)

def main():
    try:
        mass_in_kg: float = float(input("Enter mass in kg: "))
        energy_in_joules: float = mass_in_kg * (C ** 2)
        
        # Display results after calculation
        print(f"\nUsing Einstein's formula: E = m * C^2")
        print(f"Mass: {mass_in_kg} kg = {energy_in_joules} joules")
    
    except ValueError:
        print("Invalid input. Please enter a numeric value for mass.")

if __name__ == "__main__":
    main()
