def main():
    n = int(input("Enter a positive integer: "))
    is_prime = True

    for i in range(2, n // 2 + 1):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print("This is a prime number")
    else:
        print("This is not a prime number")

if __name__ == "__main__":
    main()
