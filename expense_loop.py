#!/usr/bin/env python3
"""
expense_loop.py
"""

from datetime import datetime


def get_amount():
    """ask for a valid amount in Naira"""
    while True:
        try:
            amount = float(input("  amount (₦): "))
            if amount > 0:
                return amount
            print("    number should be more than zero")
        except ValueError:
            print("    that is not a number")


def get_category():
    """ask for category or let user type custom"""
    print("  Categories: Food, Transport, Rent, Bills, Fun, Other")
    category = input("  category: ").strip().lower()
    return category if category else "other"


def get_date():
    """ask for date or use today"""
    date_str = input("  Date (YYYY-MM-DD) or press enter for today: ").strip()
    if not date_str:
        return datetime.now().strftime('%Y-%m-%d')
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return date_str
    except ValueError:
        print("    invalid date, using today")
        return datetime.now().strftime('%Y-%m-%d')


def main():
    print()
    print("-" * 50)
    print("  EXPENSE TRACKER  ")
    print("-" * 50)
    print()
    print("Add expenses one by one")
    print("Type 'done' as the category when finished")
    print()

    expenses = []

    # --- main input loop ---
    while True:
        print(f"\nexpense #{len(expenses) + 1}")
        print("-" * 30)

        category = get_category()

        if category == 'done':
            break

        amount = get_amount()
        note = input("  note (optional): ").strip()
        date = get_date()

        # store as dictionary
        expense = {
            'amount': amount,
            'category': category,
            'note': note,
            'date': date
        }
        expenses.append(expense)

        print(f"  added: ₦{amount:,.2f} for {category}")

    # --- summary with for loops ---
    print()
    print("=" * 50)
    print("  SUMMARY")
    print("=" * 50)

    if not expenses:
        print()
        print("  No Expenses Entered")
        print()
        return

    # total everything
    total = 0
    for e in expenses:
        total += e['amount']

    print()
    print(f"  Total Expenses: ₦{total:,.2f}")
    print(f"  Number of Entries: {len(expenses)}")

    # group by category using a dictionary
    by_category = {}
    for e in expenses:
        cat = e['category']
        if cat not in by_category:
            by_category[cat] = []
        by_category[cat].append(e)

    # print category breakdown
    print()
    print("  by category:")
    print("  " + "-" * 30)

    for cat in sorted(by_category.keys()):
        cat_expenses = by_category[cat]
        cat_total = 0
        for e in cat_expenses:
            cat_total += e['amount']

        print(f"    {cat:12s} ₦{cat_total:>10,.2f}  ({len(cat_expenses)} items)")

    print("  " + "-" * 30)

    # list all entries
    print()
    print("  all entries:")
    print("  " + "-" * 45)

    for i, e in enumerate(expenses, 1):
        note_str = f" ({e['note']})" if e['note'] else ""
        print(f"  {i}. {e['date']}  ₦{e['amount']:>10,.2f}  {e['category']:10s}{note_str}")

    print("  " + "-" * 45)
    print()
    print("=" * 50)


if __name__ == "__main__":
    main()
input("\n  press enter to exit...")
