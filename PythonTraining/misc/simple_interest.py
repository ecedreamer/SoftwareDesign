"""
Write a program to calculate simple interest and  amount of a given sum of money with given interest rate on given amount of time. Use separate functions to calculate the interest and amount. 
"""

def calculate_interest(p, t, r):
    interest = (p * t * r) / 100
    return interest

def calculate_amount(p, s_i):
    return p + s_i

def main():
    print("Starting interest calculator software...")

    principal = int(input("Enter principal: "))
    interest_rate = float(input("Enter interest rate: "))
    time = float(input("Enter time in year: "))

    simple_interest = calculate_interest(principal, time, interest_rate)
    print("Interest for Rs.", principal, "is Rs.", simple_interest)
    total_amount = calculate_amount(principal, simple_interest)
    print("Total amount is Rs.", total_amount)



main()