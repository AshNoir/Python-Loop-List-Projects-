# Shopping Cart System 🛒
# This program takes items and their prices
# and calculates total bill with discount


# Empty lists to store item names and prices
items = []
prices = []


# Taking number of items from user
itm = int(input("How many items do you want to add: "))


# Checking if cart is empty
if itm == 0:

    print("The cart is empty!")


else:

    # Taking item details from user
    for i in range(itm):

        # Taking item name
        item = input(f"Enter item {i+1}: ")

        # Taking item price
        price = int(input("Enter the price: "))


        # Adding item and price into lists
        items.append(item)
        prices.append(price)



    # Display shopping cart
    print("\nShopping Cart:")


    # zip combines item list and price list
    # Example: Apple + 50
    for item, price in zip(items, prices):

        print(f"{item} - ₹{price}")



    # Calculating total bill
    total = sum(prices)


    print(f"Total Bill: ₹{total}")



    # Applying 10% discount if bill > 500
    if total > 500:

        total = total - (total * 10 / 100)

        print("Discount: 10%")

        print(f"Final Bill: ₹{total}")
