age = 23
accident_count= 2
if age < 25:
    premium = 3000
else:
    premium = 2000

premium += accident_count * 500
if premium > 5000:
    print("High Risk")
else:
    print("Standard")
