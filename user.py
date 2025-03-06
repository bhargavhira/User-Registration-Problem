import re
# Mobile number must be in the format: two digits, space, and then 10 digits (e.g. 91 9919819801).
mobile = input("Enter a valid mobile number (e.g. 91 9919819801): ")
while not (len(mobile) == 13 and mobile[2] == ' ' and mobile[:2].isdigit() and mobile[3:].isdigit()):
    print("Invalid mobile number format.")
    mobile = input("Enter a valid mobile number (e.g. 91 9919819801): ")

print("\nUser Registration Successful!")
print("First Name:", first_name)
print("Last Name:", last_name)
print("Email:", email)
print("Mobile:", mobile)

