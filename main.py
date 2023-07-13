# This program calculates the bill for renting a venue
# It asks the user how many days they are going to stay
print("How many days are you going to stay?")
# Convert the input from the user to an integer
days = int(input())
# Define the constants for the rates and fees
rate = 15000 # The rental rate per day
soundSys = 4500 # The fee for using the sound system
decorFee = 3000 # The fee for decorating the venue
catering = 35000 # The fee for catering service
tax_rate = .12 # The tax rate (12%)
# Calculate the rental fee by multiplying the rate by the number of days
rental_fee = rate * days
# Calculate the total amount by adding the rental fee and other fees
total_amount = (rental_fee + soundSys + decorFee + catering)
# Calculate the tax by multiplying the total amount by the tax rate
tax = (total_amount * tax_rate)
# Calculate the final bill by adding the total amount and the tax
bill = (total_amount + tax)
# Display the bill to the user, converting it to a string
print("This is your bill: " + str(bill))
