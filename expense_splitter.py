def split_expenses():
    """
    Splits expenses among friends based on the total amount spent and the number of friends.
    """

    try:
        total = float(input("Enter total amount spent: $"))
        num_people = int(input("Enter number of people: "))

        people = []
        for i in range(num_people):
            name = input(f"Enter name of person {i + 1}: ")
            people.append(name)

        split_amount = round(total / num_people, 2)

        print("\nExpense Split:")
        for person in people:
            print(f"{person} owes: ${split_amount}")

    except ValueError:
        print("Invalid input! Please enter numeric values for amount and number of people.")

if __name__ == "__main__":
    split_expenses()

