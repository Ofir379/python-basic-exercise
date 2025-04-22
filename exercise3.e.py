spell_power = 85
accuracy = 90
control = 78
average_score = (spell_power + accuracy + control) / 3
if spell_power < 40 or accuracy < 40 or control < 40:
    result = "Fail"
elif average_score >= 90:
    result = "Archmage"
elif average_score >= 75:
    result = "Mage"
elif average_score >= 60:
    result = "Apprentice"
else:
    result = "Fail"

print(result)

