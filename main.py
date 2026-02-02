import json
from database import create_table, insert_expenses
from datetime import date

# Loads expense list
def load_from_file():
    try:
        with open("expenses.json", "r") as f:
                return json.load(f) # goes from JSON to python
    except FileNotFoundError:
        return [] # changed from dict to list

# saves expense list        
def save_to_file():
    with open("expenses.json", "w") as f:
        json.dump(expense_list, f) # goes from python to JSON


# adds expense to dict. expense description : amount
def add_expense():
    item = input("What item are you adding to your expense?\n")
    try:
        num = float(input("How much money would you like to add?\n"))
    except ValueError:
        print("Please enter in digits.")
        return
    date_added = str(date.today()) # adds the date when the entry was made


    insert_expenses(date_added, num, item, "") # calls sql function in database.py

    # expense_list.append({"Item": item, 
    #                     "Amount" : num, 
    #                     "Date added" : date_added}) # list of dicts

    # expense_list.update({item : num})

    # save_to_file()

# views expenses
def view_expense():

    for expense in expense_list: # for each dict in my list of dicts(item : item, amount : num, date added: date added) 
        print("Item:", expense["Item"], "Value:", expense["Amount"], "Date added:", expense["Date added"])
    
    total = []
    for expense in expense_list:
        total.append(expense["Amount"])
    t = sum(total)
    print("Your total is:", str(t))
        

# =========== Start of core logic ============
create_table()
# making expense dictionary -> expense description : amount
expense_list = load_from_file()

print("Welcome to the Finance Tracker.\n")


while True:

    welcome = input("Press Y to add / view expenses. Press N to exit.\n")

    # User chooses to quit application
    if welcome.lower() == 'n' or welcome.lower() == "no":
        print("Goodbye!")
        break

    # User chooses to use application
    elif welcome.lower() == 'y' or welcome.lower() == "yes":
        ask = input("Press 1. to add to expense, \nPress 2. to view Expense, \nPress 3. Exit\n")
        try:
            if int(ask) == 1: # add to expense
                add_expense()

            elif int(ask) == 2: # view expense
                view_expense()

            elif int(ask) == 3: # exit application
                print("Thank you for using the expense tracker. GoodBye!")
                break
            else:
                print("Please pick a valid option 1. or 2. or 3.\n")
        except ValueError:
            print("Please Enter a number.\n")
        

    # User has not entered a valid command
    else:
        print("Please enter a valid command!\n")
