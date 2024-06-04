initial_deposit = float(input("Enter the initial deposit: "))
cost = 800000
down_payment = cost * 0.25
low = 0.0
high = 1.0
tolerance = 100  # Within $100 of the down payment
steps = 0
if initial_deposit >= down_payment:
    r = 0.0
else:
    while True:
        r = (high + low) / 2
        amount_saved = initial_deposit * (1 + r / 12) ** 36
        steps += 1
        
        if abs(amount_saved - down_payment) <= tolerance:
            break
        elif amount_saved < down_payment:
            low = r
        else:
            high = r
        
        # Infinite loop safeguard
        if steps > 100:
            r = None
            break

print(f"Best savings rate: {r}")
print(f"Steps in bisection search: {steps}")
