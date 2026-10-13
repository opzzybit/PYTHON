print("Discount Eligibility")

total_bill = int(input("""Enter Total Bill Number :   
"""))
member = str(input("""Are you a member?, 'YES' or  'NO' :
"""))

if total_bill >= 1000 and  member == 'yes':
    print("10% off")
if total_bill >= 1000 and  member == 'no':
        print("5% off")
else:
    print("no discount print final amount, and discount message")
