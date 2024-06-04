## 6.100A PSet 1: Part B
## Name:
## Time Spent:
## Collaborators:

##########################################################################################
## Get user input for yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise below ##
##########################################################################################
yearly_salary = float(input("Enter your yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save as a decimal: "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
portion_down_payment = 0.25
r = 0.05
amount_saved = 0.0
num_of_months = 0
down_payment = cost_of_dream_home * portion_down_payment

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################
while amount_saved < down_payment:
    # Add the monthly savings from salary
    amount_saved += (yearly_salary / 12) * portion_saved
    # Add the monthly interest
    amount_saved += amount_saved * (r / 12)
    num_of_months += 1
    # Apply semi-annual raise
    if num_of_months % 6 == 0:
        yearly_salary *= (1 + semi_annual_raise)
    
print(f"Number of months: {num_of_months}")
