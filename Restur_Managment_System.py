# in this project we made a Resturant Management System
# First we create a menu Card

Menu = {
    "Pizza" : 850,
    "Burger" : 250,
    "Ice Cream" : 100,
    "Coffee" : 70,
    "Pasta" : 200,
    "Chips" : 120,
    "ChickenPiece" : 150,
    "Tea" : 60,
}

print("Welcome to in our Resturant App")
print("Pizza = Rs.850\n""Burger = Rs.250\n""Ice Cream = Rs.100\n""Coffee = Rs.70\n""Pasta = Rs.200\n""Chips = Rs.120\n""ChickenPiece = Rs.150\n""Tea = Rs.60\n")

Total_order = 0 # Total_order
# first Option
item_1 = input("Enter your Item which you want to order : ")
if item_1 in Menu:
    Total_order += Menu[item_1]
    print(f"Your Select {item_1} has been added in your order list ")
else:
    print(f"Sorry! Your Selected {item_1} item is not available now : ")

# second Option
another_item = input("If you want to add another item in your order list select (Yes/No) ")
if another_item == "Yes":
    item_2 = input("Enter your next item which you want to order : ")
    Total_order += Menu[item_2]
    print(f"Your Select {item_2} has been added in your order list ")
else:
    print(f"Sorry! Your Selected item is not available now : ")

# Third Option
third_item = input("If you want to add another item in your order list select (Yes/No) ")
if third_item == "Yes":
    item_3 = input("Enter your next item which you want to order : ")
    Total_order += Menu[item_3]
    print(f"Your Select {item_3} has been added in your order list ")
else:
    print(f"Sorry! Your Selected item is not available now : ")

print("The Total Amount which you pay now is : Rs:",Total_order)
print("............Thanks for using this Service............")