password = input("Enter your password: ")

upper_found = False
for ch in password:
    if ch >= "A" and ch <= "Z":
        upper_found = True
        break
if upper_found:
    print("Rule2 passed: Password has at least one uppercase letter.")
else:
    print("Rule2 failed: Password must have at least one uppercase letter.")