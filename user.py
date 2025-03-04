import re
# Use Case 3: Validate Email Address
# Email must have a pattern like: abc or abc.xyz, then @, then domain like bl, then dot, then extension like co, with an optional extra dot and extension.
email = input("Enter a valid email: ")
pattern = r'^[a-z]+(\.[a-z]+)?@[a-z]+\.[a-z]{2,}(\.[a-z]{2,})?$'
while not re.match(pattern, email):
    print("Invalid email address.")
    email = input("Enter a valid email: ")