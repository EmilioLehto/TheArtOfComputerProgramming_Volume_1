def gcd(m, n):
    while n != 0:
        m, n = n, m % n
    return m

if __name__ == "__main__":
    print("Euclid's algorithm")
    print("This algorithm will find the greatest common divisor between two positive Integers")

    while True:
        try:
            firstInteger = int(input("Choose your first positive Integer: "))
            secondInteger = int(input("Choose your second positive Integer: "))
            if firstInteger <= 0 or secondInteger <= 0:
                print("Please enter positive integers.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Swap the input values if necessary to ensure that m is the larger value
    if firstInteger < secondInteger:
        firstInteger, secondInteger = secondInteger, firstInteger

    print("The GCD of", firstInteger, "and", secondInteger, "is:", gcd(firstInteger, secondInteger))
         