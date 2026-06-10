#!/usr/bin/env python3
"""
password_checker.py

Checks how strong a password is and gives tips to improve it.
Run it and type a password to see the verdict.
"""

import re
from datetime import datetime


def check_length(password):
    """longer is better"""
    length = len(password)
    if length >= 12:
        return 2, "good length"
    elif length >= 8:
        return 1, "okay but could be longer"
    else:
        return 0, "too short - aim for 12+ characters"


def check_uppercase(password):
    """need at least one capital letter"""
    if re.search(r'[A-Z]', password):
        return 1, "has uppercase"
    return 0, "add a capital letter"


def check_lowercase(password):
    """need at least one lowercase letter"""
    if re.search(r'[a-z]', password):
        return 1, "has lowercase"
    return 0, "add a lowercase letter"


def check_digits(password):
    """need at least one number"""
    if re.search(r'\d', password):
        return 1, "has digits"
    return 0, "add some numbers"


def check_special(password):
    """special characters make it stronger"""
    if re.search(r'[!@#$%^&*(),.?":{}|<>\[\]\\;\'/`~_+=\-]', password):
        return 2, "has special characters"
    return 0, "add special chars like !@#$%"


def check_common(password):
    """check against common weak passwords"""
    common = ['password', '123456', 'qwerty', 'abc123', 'letmein', 'welcome', 'monkey', 'dragon']
    lower = password.lower()
    for bad in common:
        if bad in lower or lower in bad:
            return -2, f"too common - '{bad}' is a terrible password"
    return 0, "not a common password"


def check_patterns(password):
    """reject obvious patterns"""
    # repeated characters
    if re.search(r'(.)\1{2,}', password):  # aaa, 1111
        return -1, "repeated characters detected"

    # sequential numbers
    if re.search(r'123|234|345|456|567|678|789|890', password):
        return -1, "sequential numbers detected"

    # sequential letters
    if re.search(r'abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz', password.lower()):
        return -1, "sequential letters detected"

    return 0, "no obvious patterns"


def evaluate_password(password):
    """run all checks and return score + feedback"""
    checks = [
        check_length(password),
        check_uppercase(password),
        check_lowercase(password),
        check_digits(password),
        check_special(password),
        check_common(password),
        check_patterns(password),
    ]

    score = sum(c[0] for c in checks)
    feedback = [c[1] for c in checks if c[0] <= 0]  # only show issues

    return score, feedback


def get_strength_label(score):
    """convert score to human-readable label"""
    if score <= 2:
        return "WEAK", "this password is easily cracked"
    elif score <= 4:
        return "MEDIUM", "decent but not great"
    elif score <= 6:
        return "STRONG", "solid password"
    else:
        return "VERY STRONG", "excellent password"


def main():
    print()
    print("-" * 50)
    print("  PASSWORD STRENGTH CHECKER")
    print("-" * 50)
    print()
    print("type a password to check (won't be saved anywhere)")
    print("type 'quit' to exit")
    print()

    while True:
        password = input("password: ")

        if password.lower() == 'quit':
            print()
            print("stay safe out there!")
            break

        if not password:
            print("  c'mon, type something")
            continue

        score, feedback = evaluate_password(password)
        label, description = get_strength_label(score)

        print()
        print(f"  score: {score}/8")
        print(f"  strength: {label}")
        print(f"  ({description})")

        if feedback:
            print()
            print("  tips to improve:")
            for tip in feedback:
                print(f"    - {tip}")
        else:
            print()
            print("  no issues found - nice work!")

        print()
        print("-" * 50)


if __name__ == "__main__":
    main()
