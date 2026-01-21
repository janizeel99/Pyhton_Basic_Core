#write a fibonaci using recursion.
newterm = int(input("How Many Terms:"))

def rec_fib(n):
    if  n <= 1:
        return n
    else:
        return(rec_fib(n-1)+rec_fib(n-2))

if newterm <= 0:
    print("Please enter a positive integer")
else:
    for i in range(newterm):
        print(rec_fib(i))        
