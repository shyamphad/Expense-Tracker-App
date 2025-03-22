# expense_tracker.py
# This program helps track and analyze personal expenses
# It allows users to add expenses, view category totals, and see spending statistics

import csv
import os
from datetime import datetime

def main():
    """
    Main function that runs the expense tracker program.
    Handles the main menu and user interaction flow.
    """
    # Initialize the list that will hold all expense records
    expenses = []
    file_path = "expenses.csv"
    
    # Load existing expenses if the file exists
    if os.path.exists(file_path):
        expenses = load_expenses_from_csv(file_path)
        print(f"Loaded {len(expenses)} expenses from file.")
    else:
        print("No existing expense file found. Starting fresh.")
    
    # Main program loop - continue until user chooses to exit
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip().lower()
        
        # Handle the user's menu choice
        if choice == '1' or choice == 'add':
            add_expense(expenses)
            save_expenses_to_csv(expenses, file_path)
        elif choice == '2' or choice == 'view':
            view_expenses(expenses)
        elif choice == '3' or choice == 'stats':
            show_statistics(expenses)
        elif choice == '4' or choice == 'exit':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def display_menu():
    """
    Displays the main menu options to the user.
    """
    print("\n===== Expense Tracker Menu =====")
    print("1. Add a new expense")
    print("2. View expense totals by category")
    print("3. Show expense statistics")
    print("4. Exit program")
    print("================================")

def load_expenses_from_csv(file_path):
    """
    Loads expense data from a CSV file.
    
    Args:
        file_path (str): Path to the CSV file
        
    Returns:
        list: List of expense dictionaries
    """
    expenses = []
    
    try:
        with open(file_path, 'r', newline='') as file:
            reader = csv.reader(file)
            # Skip the header row
            next(reader, None)
            
            # Process each row in the CSV
            for row in reader:
                if len(row) >= 4:  # Ensure the row has all required fields
                    expense = {
                        "date": row[0],
                        "amount": float(row[1]),
                        "category": row[2],
                        "description": row[3]
                    }
                    expenses.append(expense)
    except Exception as e:
        print(f"Error loading expenses: {e}")
    
    return expenses

def save_expenses_to_csv(expenses, file_path):
    """
    Saves the expense data to a CSV file.
    
    Args:
        expenses (list): List of expense dictionaries
        file_path (str): Path to the CSV file
    """
    try:
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            # Write header row
            writer.writerow(["Date", "Amount", "Category", "Description"])
            
            # Write each expense as a row
            for expense in expenses:
                writer.writerow([
                    expense["date"],
                    expense["amount"],
                    expense["category"],
                    expense["description"]
                ])
        print(f"Expenses saved to {file_path}")
    except Exception as e:
        print(f"Error saving expenses: {e}")

def get_valid_date_from_user():
    """
    Gets a valid date from the user in MM/DD/YYYY format.
    
    Returns:
        str: Validated date string
    """
    while True:
        date_str = input("Enter date (MM/DD/YYYY) or 'today' for today's date: ").strip()
        
        # Handle 'today' shortcut
        if date_str.lower() == 'today':
            return datetime.now().strftime("%m/%d/%Y")
        
        # Validate the date format and possibility
        try:
            date_obj = datetime.strptime(date_str, "%m/%d/%Y")
            return date_str
        except ValueError:
            print("Invalid date format or impossible date. Please use MM/DD/YYYY.")

def add_expense(expenses):
    """
    Adds a new expense to the expense list based on user input.
    
    Args:
        expenses (list): List of expense dictionaries to add to
    """
    print("\n----- Add New Expense -----")
    
    # Get date
    date = get_valid_date_from_user()
    
    # Get and validate amount
    while True:
        try:
            amount_str = input("Enter amount: $").strip()
            amount = float(amount_str)
            if amount < 0:
                print("Amount cannot be negative. Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid amount. Please enter a number.")
    
    # Get category and description
    category = input("Enter category: ").strip().capitalize()
    while not category:
        print("Category cannot be empty.")
        category = input("Enter category: ").strip().capitalize()
    
    description = input("Enter description: ").strip()
    
    # Create the expense record and add it to the list
    new_expense = {
        "date": date,
        "amount": amount,
        "category": category,
        "description": description
    }
    
    expenses.append(new_expense)
    print(f"Expense of ${amount:.2f} for {category} added successfully!")

def view_expenses(expenses):
    """
    Displays expense totals grouped by category.
    
    Args:
        expenses (list): List of expense dictionaries
    """
    if not expenses:
        print("No expenses to show.")
        return
    
    # Calculate totals for each category
    category_totals = {}
    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        
        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount
    
    # Display the category totals
    print("\n----- Expense Totals by Category -----")
    for category, total in sorted(category_totals.items()):
        print(f"{category}: ${total:.2f}")
    
    # Calculate and display the grand total
    total_spent = sum(category_totals.values())
    print(f"\nTotal Spent: ${total_spent:.2f}")

def show_statistics(expenses):
    """
    Calculates and displays various statistics about the expenses.
    
    Args:
        expenses (list): List of expense dictionaries
    """
    if not expenses:
        print("No expenses to show statistics for.")
        return
    
    # Calculate total spent
    total_spent = sum(expense["amount"] for expense in expenses)
    
    # Find highest expense
    highest_expense = max(expenses, key=lambda x: x["amount"])
    
    # Calculate category totals and percentages
    category_totals = {}
    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        
        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount
    
    # Calculate percentages
    category_percentages = {}
    for category, total in category_totals.items():
        percentage = (total / total_spent) * 100
        category_percentages[category] = percentage
    
    # Display statistics
    print("\n----- Expense Statistics -----")
    print(f"Total Spent: ${total_spent:.2f}")
    print(f"Highest Expense: ${highest_expense['amount']:.2f} for " +
          f"{highest_expense['category']} on {highest_expense['date']} " +
          f"({highest_expense['description']})")
    
    # Display category breakdown with ASCII chart
    print("\nSpending Breakdown by Category:")
    for category, percentage in sorted(category_percentages.items(), 
                                      key=lambda x: x[1], reverse=True):
        bar_length = round(percentage / 2)  # Scale for display
        bar = "█" * bar_length
        print(f"{category}: {percentage:.1f}% {bar}")

# Call the main function when the script is run
if __name__ == "__main__":
    main()