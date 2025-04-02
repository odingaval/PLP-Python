def calculate_discount(price, discount_percent):
    """Calculate the final price after applying a discount."""
    if discount_percent >= 20:
        return price - (price * discount_percent / 100)
    return price  # Return original price if discount is less than 20%

# Get user input
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(original_price, discount_percentage)

# Print the result
print(f"The final price after applying the discount is: ${final_price:.2f}")
