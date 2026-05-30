# features of the expense tracker for now:
# add expense
# view all expense
# view total expense
# category search
# date range function with total
# over spending
# exit

""" incomplete task ->>warning of over spending or out of budget
2 kam kar na ha yaha ak budget lana ex 5000 or dusra user ko dikhana budget itna tha 
spend it ho gaya ha agar budget diya hua budget sa jada ha to warning dana ha the spending
is more then the given budget of the month 
pseudo code 
1.budget of month 
2. track of the expense 
3 if spending goes above the expense warning to user the 
spending is going above the budget 






"""
from datetime import datetime
print("Welcome to Expense Tracker")


def expense():
    user_exp = int(input("Enter your todays expense:"))
    user_date = input("Enter the date ").lower()
    user_desc = input("Enter the description of the expense").lower()
    user_category = input("Enter the category of the expense")
    content = (f"Date:{user_date}\n"
               f"Expense:{user_exp}\n"
               f"Description:{user_desc}\n"
               f"Category:{user_category}\n"
               "\n"

               )
    with open("expense.txt", "a")as file:
        file.write(content)
    print("The expense has saved with all details")


def view_all():
    with open("expense.txt", "r")as file:
        for line in file:
            print(line.strip())


def total_exp():
    total = 0.0
    with open("expense.txt", "r")as file:
        for line in file:
            line = line.strip()
            if line.lower().startswith("expense:"):
                total += float(line.split(":")[1])
    print(f"total expense:{total}")
    return total


def category():
    search_category = input("Enter the category to search")
    record = {}
    with open("expense.txt", "r")as file:
        for line in file:
            line = line.strip()
            if line.startswith("Date:"):
                record["date"] = line.split(":", 1)[1].strip()
            elif line.startswith("Expense:"):
                record["expense"] = line.split(":", 1)[1].strip()
            elif line.startswith("Description:"):
                record["desc"] = line.split(":", 1)[1].strip()
            elif line.startswith("Category:"):
                record["category"] = line.split(":", 1)[1].strip().lower()
            elif line == "":
                if record.get("category") == search_category:
                    print(f"Date:{record['date']}")
                    print(f"Expense:{record['expense']}")
                    print(f"Description:{record['desc']}")
                    print(f"Category:{record['category']}")
                    print("*"*20)
                    record = {}
    if record.get("category") == search_category:
        print(
            record["date"],
            record["expense"],
            record["desc"],
            record["category"],
            sep="\n"
        )
        print("-"*20)


def date_filter():
    search_from = input(
        "Enter the date you want to search from (dd//mm//yyyy):")
    search_to = input("Enter the date you want to search to(dd//mm//yyyy):")
    start_date = datetime.strptime(search_from, "%d/%m/%Y")
    end_date = datetime.strptime(search_to, "%d/%m/%Y")

    record = {}
    total = 0.0
    found = False

    with open("expense.txt", "r")as file:
        for line in file:
            line = line.strip()
            if line.startswith("Date"):
                record["date"] = datetime.strptime(
                    line.split(":", 1)[1].strip(),
                    "%d/%m/%Y"
                )
            elif line.startswith("Expense"):
                record["expense"] = float(line.split(":", 1)[1].strip())
            elif line.startswith("Description"):
                record["desc"] = line.split(":", 1)[1].strip()
            elif line.startswith("Category"):
                record["category"] = line.split(":", 1)[1].strip()
            elif line == "":
                if start_date <= record.get("date") <= end_date:
                    found = True
                    print(f"Date: {record['date'].strftime('%d/%m/%Y')}")
                    print(f"Expense: {record['expense']}")
                    print(f"Description: {record['desc']}")
                    print(f"Category: {record['category']}")
                    print("-"*20)

                    total += record["expense"]
                record = {}

    if found:
        print(
            f"Total expense from {search_from} to {search_to} : is {total}\n")
    else:
        print("No expense found for this date.")


def overspending():
    monthly_budget = int(input("Enter your monthly budget"))
    total_expense = 0
    with open("expense.txt", "r")as file:
        for line in file:
            line = line.strip().lower()
            if line.startswith("expense"):
             amount = float(line.split(":", 1)[1].strip())
             total_expense += amount
    if total_expense > monthly_budget:
        overspend=monthly_budget -total_expense
        print(f"your overspending [{overspend}]")
    else:
        remaining=total_expense-monthly_budget
        print(f"you are in budget [{remaining}]")


while True:
    print("1.Add the expense ")
    print("2.view all the expense")
    print("3.total expense")
    print("4.category ")
    print("5 search by date")
    print("6.overspending")
    print("7.Exit")

    message = int(input("Enter the number "))

    if message == 1:
        expense()
    elif message == 2:
        view_all()
    elif message == 3:
        total_exp()
    elif message == 4:
        category()
    elif message == 5:
        date_filter()
    elif message == 6:
        overspending()
    elif message == 7:
        print("exiting the program")
        break
    else:
        print("please use a valid int number")
