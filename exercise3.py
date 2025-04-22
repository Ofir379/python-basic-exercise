salary = 5000
tax_rate = 0.22
net_income = salary * (1 - tax_rate)
rent = 3000
if net_income >= rent:
    print("rent is affordable")
else:
    print("not enough")
saving = 1000 
if net_income >= rent + saving:
    print ("rent and save")
elif net_income >= rent:
    print ("just rent")
else:
    print ("not enough")

