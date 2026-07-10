#PROJECT 2 - PART 1 - EXPENSE TRACKER

import json
from datetime import datetime
expenses = {"Groceries":[], "Fuel":[] ,"Snacks":[] ,"Phone Bill":[], "Medicine":[], "TV/Internet Bill":[], "Laundry/Ironing":[], "OneTime Expenses":[]}
categories= list(expenses)

#FUNCTIONS

def Display_Categories():
    print("======= Categories ========")

    for i, category in enumerate(categories, start=1):
        print(i, ".", category)

def Get_Category():
    while True:
        try:
            category_choice=int(input("Enter the choice of your category:"))
            if 1 <= category_choice <= len(categories):
                select_category=categories[category_choice-1]
                break
            else:
                print("Invalid Category. Try again.")
        except ValueError:
            print("Invalid Choice. Try again.")
    return select_category
    
def Add_Expenses():

    Display_Categories()

    # GET VALID CATEGORY
    selected_category =Get_Category()
    
    # GET AMOUNT (outside category loop)
    while True:
        try:
            expense_name=input("Enter the expense name:")
            while True:
                date=input("Enter the date:")
                try:
                    datetime.strptime(date, "%d-%m-%Y")
                    break
                except ValueError:
                    print("Invalid date")
            amount = int(input("Enter the expense amount: "))
            if amount<=0:
                print("Oops! The amount must be positive.")
                continue
            expense={"name":expense_name,"date":date,"amount":amount}
            expenses[selected_category].append(expense)
            Save_Data()
            print("Expense added ✔")
            break
        except ValueError:
            print("Invalid amount. Try again.")

def Display_Category(category):
    if not expenses[category]:
            print("There are no expenses to display.")
            return
    for i,expense in enumerate(expenses[category],start=1):
        print(f" {i}. {expense['name']:12} | {expense['date']:20} | {expense['amount']:>8}")
    print()
    
def View_Summary():
    print("======= Monthly Summary =======")
    for category in expenses:
        summ=0
        for expense in expenses[category]:
            summ+=expense["amount"]
        print(f"{category:20} ₹{summ}")
 

def View_All_Expenses():
    print("======= All Expenses =======")
    for category in expenses:
        print("========", category ,"========")
        if not expenses[category]:
            print("No expense added yet")
        else:
            for i,expense in enumerate(expenses[category],start=1):
                print(f"{i}. {expense['name']:12} | {expense['date']:20} | {expense['amount']:>8}")
                print()
            total = 0
            for expense in expenses[category]:
                total += expense["amount"]

            print("-"*50)
            print("Total =", total)

def Load_Data():
    global expenses
    try:
        with open("expenses.json",'r') as file:
            expenses = json.load(file)       
    except FileNotFoundError:
        print("File not found. Starting fresh.")

def Save_Data():
    with open("expenses.json",'w') as file:
        json.dump(expenses,file,indent=4)

def Delete_Expense():
    Display_Categories()
    try:
        deleting_category=Get_Category()
        Display_Category(deleting_category)
        deleting_expense_choice=int(input("Enter your choice of expense to be deleted:"))
        if 1 <= deleting_expense_choice <= len(expenses[deleting_category]):
            expenses[deleting_category].pop(deleting_expense_choice -1)
            print("The expense has been deleted.")
            Save_Data()
        else:
            print("Invalid choice. Try again")
    except ValueError:                                      
        print("Invalid choice. Please enter a number")

def Edit_Expense():
    fields=['name','date','amount']
    Display_Categories()
    try:
        editing_category = Get_Category()
        Display_Category(editing_category)
        editing_expense_choice=int(input("Enter your choice of expense to be edited:"))
        if 1 <= editing_expense_choice <= len(expenses[editing_category]):
            for i, field in enumerate(fields,start=1):
                print(i,".",field.title())
            field_choice=int(input("Enter the choice of field:"))
            if 1 <= field_choice <= len(fields):
                if fields[field_choice-1]=='amount':
                    while True:
                        new=int(input("Enter the new amount:"))
                        if new<=0:
                            break
                        print("Oops! The amount must be postitive.")
                elif fields[field_choice-1]=='date':
                    while True:
                        new=input("Enter the date:")
                        try:
                            datetime.strptime(new, "%d-%m-%Y")
                            break
                        except ValueError:
                            print("Invalid date")
                else:
                    new=input("Enter the new value:")
                editing_field= fields[field_choice-1]
                editing_expense=expenses[editing_category][editing_expense_choice -1]
                editing_expense[editing_field] = new
                print("Changes have been edited")
                Save_Data()
            else:
                print("Invalid choice. Try again")
        else:
            print("Invalid choice. Try again.")
    except ValueError:
        print("Invalid input. Try again.")

def Search_Expense():
    Display_Categories()
    search_category=Get_Category()
    searching_expense=input("Enter the expense to be searched:").lower()
    for i, expense in enumerate(expenses[search_category],start=1):
        if searching_expense in expense['name'].lower():
            print(f"{i}. {expense['name']:12} | {expense['date']:20} | {expense['amount']:>8}")
        else:
            print("No expense matches.")
#MAIN BRANCH

Load_Data()

while True:
    print("======== Welcome to the Menu =========")
    print("1. Add Expenses")
    print("2. View summary")
    print("3. View all expenses")
    print("4. Edit an expense")
    print("5. Delete an Expense")
    print("6. Search Expense")
    print("7. Exit")

    try:
        choice=int(input("Choose from the Menu:"))
        if choice==1:
            Add_Expenses()
            
        elif choice==2:
            View_Summary()
            
        elif choice==3:
            View_All_Expenses()

        elif choice==4:
            Edit_Expense()

        elif choice==5:
            Delete_Expense()

        elif choice==6:
            Search_Expense()
            
        elif choice==7:
            print("Thank you. See ya later!")
            break
        
        else:
            print("Invalid choice. Try again!")
    except ValueError:
        print("Invalid Choice. Try Again.")

        

    
