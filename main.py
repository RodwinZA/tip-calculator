print("Welcome to the tip calculator!")

total_bill = input("What was the total bill? $")
tip = input("How much tip woul you like to give? 10, 12, or 15? ")
number_of_people = input("How many people to split the bill? ")

# Change types from string to float/int

total_bill = float(total_bill)
tip = float(tip)
number_of_people = int(number_of_people)

tip_amount = (total_bill / 100) * tip
split_payment = (total_bill + tip_amount) / number_of_people
print(f"Each person should pay: $" + "{0:.2f}".format(split_payment))