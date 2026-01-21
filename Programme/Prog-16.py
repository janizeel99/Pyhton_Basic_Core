#generate an infinite fibonacci series by using a generators.

def fibonacct():
    a,b = 0,1
    while True:
     yield a
     a,b=b,a+b


fibo1 = fibonacct()
print(next(fibo1))
print(next(fibo1))
print(next(fibo1))
print(next(fibo1))
print(next(fibo1))
print(next(fibo1))
print(next(fibo1))
print(next(fibo1))
print(next(fibo1))
print(next(fibo1))