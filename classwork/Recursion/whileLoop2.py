def count_down(start,end):
    
    while start > end:
        print(start)
        start -= 1

if __name__ == "__main__":
    start = int(input("Enter a number to count down from: "))
    end = int(input("Enter a number to count down to: "))

    count_down(start,end)
   