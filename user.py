import logging
import re

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

password = input("Enter your password: ")

# Rule 1: Minimum 8 characters
if len(password) >= 8:
    logging.info("Rule1 passed: Password has at least 8 characters.")
else:
    logging.error("Rule1 failed: Password must be at least 8 characters.")

# Rule 2: At least 1 uppercase letter
upper_found = False
for ch in password:
    if ch.isupper():
        upper_found = True
        break
if upper_found:
    logging.info("Rule2 passed: Password has at least one uppercase letter.")
else:
    logging.error("Rule2 failed: Password must have at least one uppercase letter.")

# Rule 3: At least 1 numeric digit
digit_found = False
for ch in password:
    if ch.isdigit():
        digit_found = True
        break
if digit_found:
    logging.info("Rule3 passed: Password has at least one numeric digit.")
else:
    logging.error("Rule3 failed: Password must have at least one numeric digit.")

# Rule 4: Exactly 1 special character from [@, #, $, %, ^, &, *]
special_chars = "@#$%^&*"
special_count = 0
for ch in password:
    if ch in special_chars:
        special_count = special_count + 1
if special_count == 1:
    logging.info("Rule4 passed: Password has exactly one special character.")
else:
    logging.error("Rule4 failed: Password must have exactly one special character from [@, #, $, %, ^, &, *].")

# Final overall check
if len(password) >= 8 and upper_found and digit_found and special_count == 1:
    logging.info("Password is valid.")
else:
    logging.info("Password is invalid.")
