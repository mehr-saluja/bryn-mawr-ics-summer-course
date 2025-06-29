
print("👋 Hello and welcome to Summertime Bar!")
print("I'm your waiter, Mehr. I'll be taking your order on this lovely day today.")

menu = {
    "Drink": ["Water", "Soda", "Juice"],
    "Appetizer": ["Fries", "Salad"],
    "Entree": ["Burger", "Pizza"],
    "Dessert": ["Ice Cream", "Cake"]
}

prices = {
    "Water": 1.0,
    "Soda": 2.0,
    "Juice": 2.5,
    "Fries": 3.0,
    "Salad": 4.0,
    "Burger": 8.0,
    "Pizza": 9.0,
    "Ice Cream": 3.5,
    "Cake": 4.5
}

# Wait for user to be ready
while True:
    feedback = input('\nAre you ready to order? (yes/no): ').strip().lower()
    if feedback == "yes":
        print("😊 Perfect! What can I get you to drink today?")
        break
    elif feedback == "no":
        print("Okay, take your time. Let me know when you're ready!")

order = []
total = 0.0

# Take order for each category
for category, items in menu.items():
    print(f"\n{category}:")
    for i, item in enumerate(items, 1):
        print(f"{i}. {item} (${prices[item]})")
    choice = input(f"\nWhat can I get you for {category.lower()}? (Enter number or press Enter to skip) ").strip()
    if not choice:
        print(f"Skipping {category.lower()}.")
        continue
    try:
        choice_index = int(choice) - 1
        if 0 <= choice_index < len(items):
            selected_item = items[choice_index]
            order.append(selected_item)
            total += prices[selected_item]
            print(f"You chose: {selected_item}")
        else:
            print("Invalid choice, skipping.")
    except ValueError:
        print("Invalid input, skipping.")

if order:
    print("\n🧾 Here is your order summary:")
    for item in order:
        print(f"- {item} (${prices[item]})")
    print(f"Subtotal: ${total:.2f}")
else:
    print("\nNo items ordered.")

def complete_meal_and_payment(total):
    print("✅ Everything is served. Enjoy your meal!")

    while True:
        feedback = input("\nDid you enjoy your meal? (yes/no): ").strip().lower()
        if feedback == "yes":
            print("😊 We're thrilled to hear that! Thank you for dining with us.")
            break
        elif feedback == "no":
            print("😞 We're sorry to hear that. Your feedback helps us improve.")
            break
        else:
            print("Please enter 'yes' or 'no'.")

    while True:
        tip_input = input("\nWould you like to leave a tip? Enter tip percentage (e.g., 15): ").strip()
        if not tip_input:
            tip_percent = 0
            break
        try:
            tip_percent = int(tip_input)
            if tip_percent < 0:
                print("Please enter a positive percentage.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

    tip_amount = round((tip_percent / 100) * total, 2)
    final_total = round(total + tip_amount, 2)

    print(f"💵 Tip amount: ${tip_amount:.2f}")
    print(f"💰 Final total (with tip): ${final_total:.2f}")


if order:
    complete_meal_and_payment(total)
