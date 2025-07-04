# This program multiplies two numbers using recursion
def multiply(count,n):
    if count == 0:
        return 0
    else:
        return n + multiply(count - 1 ,n)

if __name__ == "__main__":
    n = int(input("Enter 1st number: "))
    m = int(input("Enter 2nd number: "))
    result = multiply(m,n)
    print(result)