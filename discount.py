order_amount = float(input("Enter order amount: "))
customer_type = input("Enter customer type (regular/member/vip): ").lower()
coupon_code = input("Enter coupon code (if any): ")


total = order_amount


if order_amount < 50:
    total += order_amount * 0.05


if customer_type in ("member", "vip"):
    total -= total * 0.10

if customer_type == "vip" and coupon_code == "SAVE15":
    total -= total * 0.15

print(f"Final total: ${total:.2f}")


