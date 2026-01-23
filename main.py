# making expense dictionary -> expense description : amount
expense_list = {}

# adds expense to dict. expense description : amount
def add_expense():
    item = input("What item are you adding to your expense?\n")
    num = float(input("How much money would you like to add?\n"))

    expense_list.update({item : num})

# views expenses
def view_expense():
    print("Your expense log is:\n", expense_list)

    # calculate total expense
    total = 0.0
    for value in expense_list.values():
        total += value
    print("Your total cost of expenses are: $" + str(total))
        


print("Welcome to the Finance Tracker.\n")


while True:

    welcome = input("Press Y to add or view expenses. Press N to exit.\n")

    # User chooses to quit application
    if welcome.lower() == 'n' or welcome.lower() == "no":
        print("Goodbye!")
        break

    # User chooses to use application
    elif welcome.lower() == 'y' or welcome.lower() == "yes":
        ask = int(input("Type 1. to add to expense, 2. to view Expense, 3. Exit\n"))
        if ask == 1: # add to expense
            add_expense()

        elif ask == 2: # view expense
            view_expense()

        elif ask == 3: # exit application
            print("Thank you for using the expense tracker. GoodBye!")
            break

        else:
            print("Please pick a valid option 1. or 2. or 3.\n")
        

    # User has not entered a valid command
    else:
        print("Please enter a valid command!\n")
