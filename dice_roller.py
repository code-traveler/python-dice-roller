import random

def roll_dice(n):
    print(f"\nRolling {n} dice...")
    for i in range(1, n + 1):
        value = random.randint(1, 6)
        print(f"Dice {i}: 🎲 {value}")
    print()

def main():
    print("🎲 Welcome to the Dice Roller!")
    
    while True:
        try:
            num = int(input("How many dice do you want to roll? "))
            if num <= 0:
                print("Please enter a positive number.")
                continue
            roll_dice(num)
        except (ValueError, EOFError):
            print("\nInput interrupted or invalid. Exiting.")
            break

        again = input("Do you want to roll again? (y/n): ").strip().lower()
        if again != 'y':
            print("Goodbye! 👋")
            break

if __name__ == "__main__":
    main()
