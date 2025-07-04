def count_down(n):
    if n == 0:
        return 1
    else:
        print(n)
        return count_down(n - 1)


if __name__ == "__main__":
    n = 10
    count_down(n)     

