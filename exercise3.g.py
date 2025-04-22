age = 20
has_gold_pass = True
is_royal = False
is_blacklisted = False
if age >= 18 and (has_gold_pass or is_royal) and not is_blacklisted:
    print ("allowed")
else:
    print ("denied")

