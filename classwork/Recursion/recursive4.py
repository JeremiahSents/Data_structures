def is_prime(n, count):
    if count == 1:
        print(f"{n} is a prime number")
        return True
    elif n % count == 0:
        print(f"{n} is not a prime number")
        return False
    else:
        return is_prime(n, count - 1)

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    if n <= 1:
        print(f"{n} is not a prime number")
    else:
        is_prime(n, n - 1)
