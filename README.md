# Expense Tracker Application

A simple command-line expense tracker application built with Python that allows users to record, categorize, and analyze their spending habits.

## Features

- Add new expenses with date, amount, category, and description
- View expense totals grouped by category
- Generate statistics about spending patterns
- Save expense data to CSV for persistent storage
- Load existing expense data from CSV file
- Data validation to ensure proper input

## How to Use

1. Make sure you have Python 3.6+ installed on your system
2. Clone this repository to your local machine
3. Run the program with `python expense_tracker.py`
4. Follow the on-screen prompts to interact with the application

## Menu Options

The application offers the following options:

1. **Add a new expense** - Record a new expense with date, amount, category, and description
2. **View expense totals by category** - See a breakdown of spending by category
3. **Show expense statistics** - View detailed statistics including total spent, highest expense, and category percentages
4. **Exit program** - Save and quit the application

## Data Storage

The application stores all expense data in a CSV file named `expenses.csv` located in the same directory as the script. This file is automatically created when you add your first expense.

## Requirements

- Python 3.6+
- Standard libraries: csv, os, datetime (no additional installations required)

## Sample Usage

```
===== Expense Tracker Menu =====
1. Add a new expense
2. View expense totals by category
3. Show expense statistics
4. Exit program
================================
Enter your choice: 1

----- Add New Expense -----
Enter date (MM/DD/YYYY) or 'today' for today's date: today
Enter amount: $45.99
Enter category: Groceries
Enter description: Weekly shopping at Kroger
Expense of $45.99 for Groceries added successfully!
Expenses saved to expenses.csv

===== Expense Tracker Menu =====
1. Add a new expense
2. View expense totals by category
3. Show expense statistics
4. Exit program
================================
Enter your choice: 3

----- Expense Statistics -----
Total Spent: $45.99
Highest Expense: $45.99 for Groceries on 03/22/2025 (Weekly shopping at Kroger)

Spending Breakdown by Category:
Groceries: 100.0% █████████████████████████████████████████████████
```

## Project Structure

```
expense-tracker/
│
├── expense_tracker.py  # Main application file
├── expenses.csv        # Data storage file (created on first run)
└── README.md          # Documentation
```
