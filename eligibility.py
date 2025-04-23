age = int(input("Enter your age: "))
has_ticket = input("Do you have a ticket (y/n)? ").lower()
vip_code = input("Enter VIP code (if any): ")


if age < 0:
    print("Invalid age")
else:
   
    if (age >= 18 and has_ticket == "y") or vip_code == "GOLDVIP":
        eligible = True
    else:
        eligible = False

   
    print(f"Access granted: {eligible}")
