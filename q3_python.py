# Question 3 - String Manipulation
# Topic: Name Formatting Utility
#
# Task 1:
# Write a function called formatName(firstName, lastName) that accepts two strings
# and returns a formatted string in this format: "lastName, firstName"
# Example: formatName("John", "Smith") → "Smith, John"

# Function to format the name as "lastName, firstName"
def formatName(firstName, lastName):
    # Ensure that the first letter of each name is capitalized and return the formatted string
    return f"{lastName.capitalize()}, {firstName.capitalize()}"


# Task 2:
# Write a function called formatInitials(firstName, lastName) that returns the
# initials of the person as a string in uppercase.
# Example: formatInitials("john", "smith") → "J.S."
# Note: your function should handle inputs in any case (upper, lower, or mixed)
# and always produce properly capitalised output.

# Function to format the initials of the name
def formatInitials(firstName, lastName):
    # Extract the first letter of each name, convert to uppercase, and return in the format "F.L."
    return f"{firstName[0].upper()}.{lastName[0].upper()}."


# Task 3:
# Call both functions with the following inputs and print each result:
#   formatName("Alice", "Tan")  → Expected: "Tan, Alice"
#   formatName("bob", "lim")    → Expected: "Lim, Bob"
#   formatInitials("Alice","Tan") → Expected: "A.T."
#   formatInitials("bob","lim")   → Expected: "B.L."

# Testing the functions with the specified inputs
print(formatName("Alice", "Tan"))  # Expected: "Tan, Alice"
print(formatName("bob", "lim"))    # Expected: "Lim, Bob"
print(formatInitials("Alice", "Tan"))  # Expected: "A.T."
print(formatInitials("bob", "lim"))    # Expected: "B.L."
