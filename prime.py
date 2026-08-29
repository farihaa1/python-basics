number = int(input("Enter a positive integer: "))

is_prime = True
if number <=1:
    is_prime = False
else:
    for divisor in range(2,int(number ** 0.5)+1):
        if number%divisor ==0 :
            is_prime=False
            break
        
if is_prime:
    print("The number is prime.") 
else:
    print("The number is not a prime")       