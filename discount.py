def calculate_discount(price, discount_percent):
    # Check if discount is 20% or higher
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt the user for original price input
price = int(input("Enter the original price of the item: "))

# Prompt the user for discount percentage input
discount_percent = int(input("Enter the discount percentage: "))

# Call the function and print the result
final_price = calculate_discount(price, discount_percent)

# check if discount applied.
if final_price == price:
    print(f"No discount applied, price is: {price}")
else:
    print(f"The final price is: {final_price}")
