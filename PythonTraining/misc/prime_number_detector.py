# write a program to ask number and check whether its prime number or not

def check_prime(j):
    is_prime = True
    for i in range(2, j):
        if j % i == 0:
            is_prime = False
            break
    return is_prime

def main():
    number1 = int(input("Enter a first number: "))
    number2 = int(input("Enter a second number: "))
    if number2 <= number1:
        print("Your inputs are invalid, number 2 should be greater than number 1")
        exit()
    prime_number_list = []
    for i in range(number1, number2 + 1):
        is_this_prime = check_prime(i)
        if is_this_prime:  # equivalent to if is_this_prime is True: 
            prime_number_list.append(i)
    print(prime_number_list)


main()

