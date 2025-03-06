password = input("Enter your password: ")

# Use Case 1: Check for minimum 8 characters
if len(password) >= 8:
    print("Rule1 passed: Password has at least 8 characters.")
else:
    print("Rule1 failed: Password must be at least 8 characters.")
