def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    else:
        return price
    
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))
final_price = calculate_discount(price, discount_percent)
if final_price != price:
    print("The final price after applying the discount is: $", final_price)
else:
    print("No discount was applied. The final price is: $", price)