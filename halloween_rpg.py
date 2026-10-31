import random

inventory = []
candy_count = 0
battle_score = 0


def explore():
    global candy_count

    while True:
        print("\nExplore Menu")
        print(f"Candies on Hand: {candy_count}")
        print("1. Search Giant Pumpkin")
        print("2. Enter Haunted House (500 candies jackpot)")
        print("3. Back to main menu")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "3":
            break

        if choice not in ["1", "2"]:
            print("Invalid input")
            continue

        if choice == "1":
            candies = random.randint(1, 10)
            candy_count += candies
            print(f"You found a glowing pumpkin and {candies} pieces of candy!")
        elif choice == "2":
            outcome = random.randint(1, 10)

            if outcome == 1:
                jackpot = 500
                candy_count += jackpot
                print(f"You found a hidden candy jackpot of 500 candies!")
            else:
                candies = random.randint(10, 25)
                stolen = min(candies, candy_count)
                candy_count -= stolen
                print(f"A spooky ghost jumps out and steals {stolen} candies!")


def battle():
    global battle_score

    while True:
        print("\nBattle Menu")
        print("Battle Score:", battle_score)
        print("Inventory:", inventory)
        print("1. Fight Skeleton")
        print("2. Cast Spell on Monster")
        print("3. Back to main menu")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "3":
            break

        if choice not in ["1", "2"]:
            print("Invalid input")
            continue

        if choice == "1":
            if "sword" in inventory:
                sword_damage = random.randint(10, 25)
                print(f"You attacked the skeleton for {sword_damage} damage! You won!")
                inventory.remove("sword")  # Consumable: sword is used up
                battle_score += sword_damage
            else:
                print("You need to acquire a sword.")
        elif choice == "2":
            if "spell" in inventory:
                spell_damage = random.randint(25, 50)
                print(f"Your spell hit the monster for {spell_damage} damage! You won!")
                inventory.remove("spell")  # Consumable: spell is used up
                battle_score += spell_damage
            else:
                print("You need to acquire a spell.")


def trick_or_treat():
    global candy_count

    while True:
        print("\nTrick or Treat")
        print(f"Candies on Hand: {candy_count}")
        val_input = input("Enter number of houses (or 'B' to go back): ").strip().upper()

        if val_input == "B":
            break

        try:
            houses = int(val_input)
            if houses <= 0:
                print("Invalid input: Value must be greater than 0")
                continue

            if houses > 5:
                print("You can only visit up to 5 houses at a time!")
                continue

            candy = random.randint(5, 20) * houses
            candy_count += candy
            print(f"You visited {houses} house(s) and got {candy} candies!")
            print(f"Total Candies: {candy_count}")
        except ValueError:
            print("Invalid input")


def inventory_store():
    global candy_count

    while True:
        print("\nInventory Store")
        print("Candies on Hand:", candy_count)
        print("Inventory:", inventory)
        print("1. Acquire sword (costs 150 candies)")
        print("2. Acquire spell (costs 250 candies)")
        print("3. Back to main menu")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "3":
            break

        if choice not in ["1", "2"]:
            print("Invalid input")
            continue

        if choice == "1":
            if "sword" in inventory:
                print("Sword already acquired.")
            elif candy_count >= 150:
                candy_count -= 150
                inventory.append("sword")
                print("You acquired a sword.")
            else:
                print("You need at least 150 candies to acquire a sword.")
        elif choice == "2":
            if "spell" in inventory:
                print("Spell already acquired.")
            elif candy_count >= 250:
                candy_count -= 250
                inventory.append("spell")
                print("You acquired a spell.")
            else:
                print("You need at least 250 candies to acquire a spell.")


while True:
    print("\nHalloween RPG")
    print("")
    print("Player Stats:")
    print("Candies on Hand:", candy_count)
    print("Battle Score:", battle_score)
    print("Inventory:", inventory)
    print("")
    print("1. Explore")
    print("2. Battle")
    print("3. Trick or Treat")
    print("4. Inventory Store")

    choice = input("Enter your choice (1-4 or Q to quit): ").strip().upper()

    if choice == "Q":
        print("Closing game. Happy Halloween ^_^")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid input")
        continue

    if choice == "1":
        explore()
    elif choice == "2":
        battle()
    elif choice == "3":
        trick_or_treat()
    elif choice == "4":
        inventory_store()