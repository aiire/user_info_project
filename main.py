first_name = input("Enter your first name: ")
middle_initial = input("Enter your middle initial: ")
last_name = input("Enter your last name: ")
street_address = input("Enter your street address: ")
city = input("Enter your city: ")
state_abbreviation = input("Enter your state (as abbreviation): ")
zip_code = input("Enter your zip code: ")
phone_number = input("Enter your cell phone number: ")
email_address = input("Enter your email address: ")

# First Name Middle Initial Last Name
# Street Address
# City, State Zip Code
# Phone Number
# Email Address

if len(middle_initial.strip()) == 0:
    print(f"{first_name} {last_name}")
else:
    print(f"{first_name} {middle_initial} {last_name}")

print(street_address)
print(f"{city}, {state_abbreviation} {zip_code}")
print(phone_number)
print(email_address)
