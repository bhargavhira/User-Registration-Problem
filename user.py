password = input("Enter your password: ")

special_chars = "@#$%^&*"
special_count = 0
for ch in password:
    if ch in special_chars:
        special_count = special_count + 1
if special_count == 1:
    print("Rule4 passed: Password has exactly one special character.")
else:
    print("Rule4 failed: Password must have exactly one special character from [@, #, $, %, ^, &, *].")