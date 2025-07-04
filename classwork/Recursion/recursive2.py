def count_down(start,end):
    if start == end:
        return 1
    else:
        print(start)
        return count_down(start - 1, end)
    
if __name__ == "__main__":
    start = int(input("Enter a number to count down from: "))
    end = int(input("Enter a number to count down to: "))

    count_down(start,end)    