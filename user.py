password = input("Enter your password: ")

digit_found = False
for ch in password:
    if ch >= "0" and ch <= "9":
        digit_found = True
        break
if digit_found:
    print("Rule3 passed: Password has at least one numeric digit.")
else:
    print("Rule3 failed: Password must have at least one numeric digit.")