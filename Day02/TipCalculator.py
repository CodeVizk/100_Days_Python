print("Welcome to Tip Calculator!")
amount=float(input("Enter total amount to pay. rs-"))
tip=int(input("How much tip to give? 10 12 or 15? "))
no_of_people=int(input("How many people to split the bill. "))


tip_percent=((tip/100)+1)
total_bill=tip*amount
bill_per_person=total_bill/no_of_people
final_bill=round(bill_per_person,2)
final_bill="{:.2f}".format(bill_per_person)
print(f"Each person should pay Rs-{final_bill}")