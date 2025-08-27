# Simple Discount Calculator

# Define the function that calculates the discount
def calculate_discount(price, discount_percent):
    """Applies discount amount to give final price"""
    discount_amount = price * discount_percent / 100
    final_price = price - discount_amount
    return float(final_price)


# Start The Program !!
# Get user to input and use the fuction
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Apply discount on these condition and call the function
if discount_percent >= 20:
    final_price = calculate_discount(price, discount_percent)
    print("Final price after discount is:", final_price)
else:
    print("No discount applied. Final price is:", price)