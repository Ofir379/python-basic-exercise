item_price = 150  
quantity = 3
total_price = item_price * quantity
if total_price > 200:
    shipping_fee = 0   
else:
    shipping_fee = 20
    discount = 0
if total_price > 500:
    discount = total_price * 0.10
total_cost = total_price + shipping_fee - discount
print(f"Total cost: {total_cost}")
if discount > 0:
    print("Discount applied!")
if shipping_fee == 0:
    print("Free shipping!")
