expenses = []

while True:
    print("\n1. Add Expense")
    print("2. Show Expenses")
    print("3. Show Total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        category = input("Enter expense category: ")

        try:
            amount = float(input("Enter expense amount: "))

            if amount <= 0:
                print("Amount must be greater than zero.")
            else:
                expense = {
                    "category": category,
                    "amount": amount
                }

                expenses.append(expense)
                print("Expense added successfully.")

        except ValueError:
            print("Please enter a valid amount.")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses added yet.")
        else:
            print("\n--- Expense List ---")

            for number, expense in enumerate(expenses, start=1):
                print(number, ".", expense["category"], "-", expense["amount"])

    elif choice == "3":
        total = 0

        for expense in expenses:
            total = total + expense["amount"]

        print("Total expense is:", total)

    elif choice == "4":
        print("Thank you for using the Expense Tracker.")
        break

    else:
        print("Invalid choice. Enter a number from 1 to 4.")