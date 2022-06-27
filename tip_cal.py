bill= input("What is the bill? ")
tip_percent= input("What is the tip percentage? ")
tip_percent= float(tip_percent)/ 100 + 1 
paying_for= input("How many people are paying? ")
paying_for= int(paying_for)
tip= float(bill) / paying_for * tip_percent

print(f"Each person should pay ${tip:.2f}")
