print("Welcome! Let's calculate your net salary.")
try:
    gross = input("What is your gross salary ? ")
    gross = int(gross)
    children = input("How many children do you have ? ")
    children = int(children)

    tax_rate = None
    if gross < 1000:
        tax_rate = 10
    elif gross < 2000:
        tax_rate = 12
    elif gross < 4000:
        tax_rate = 14
    else:
        tax_rate = 18

    if gross < 2000:
        tax_rate -= children * 1
    else:
        tax_rate -= children * 0.5
    if tax_rate < 0:
        tax_rate = 0

    net = gross * (1 - tax_rate / 100)
    print(f"Your net salary is: {round(net, 2)}")
except ValueError:
    print("Please enter valid numbers.")