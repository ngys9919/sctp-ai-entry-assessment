# Question 2 - Arrays and Loops
# Topic: Inventory Tracker
#
# Task 1:
# Declare an empty list called inventory to store item names as strings.

# Declare an empty list called inventory
inventory = []


# Task 2:
# Write a function called addItem(itemName) that adds the given item to the
# inventory list. If the item already exists, print a message instead of adding it.
# Example message: "Mouse is already in inventory."

# Function to add an item into the inventory
def addItem(itemName):
    # Check if the item already exists in the inventory
    if itemName in inventory:
        # If it exists, print a message
        print(f"{itemName} is already in inventory.")
    else:
        # If it does not exist, add it to the inventory
        inventory.append(itemName)


# Task 3:
# Write a function called listInventory() that prints all items in the inventory.
# If the inventory is empty, print: "Inventory is empty."

# Function to list all items in the inventory
def listInventory():
    # Check if the inventory is empty
    if len(inventory) == 0:
        # If it is empty, print a message
        print("Inventory is empty.")
    else:
        # If it is not empty, print the inventory
        print("Inventory:", inventory)


# Task 4:
# Call the functions in this order and observe the output:
addItem("Laptop")
addItem("Mouse")
addItem("Keyboard")
addItem("Mouse")   # Should trigger duplicate warning
listInventory()

# Expected output:
# Mouse is already in inventory.
# Inventory: ['Laptop', 'Mouse', 'Keyboard']
