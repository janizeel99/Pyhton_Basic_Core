import math

try:
    value = input("Enter a number: ")
    print("You entered:", value)

    num = float(value)

    if num < 0:
        print("Error: Cannot Calculate Square Root Of A Negative Number.")
    else:
     result = math.sqrt(num)
     print(f"Square root of {num} is {result}")

except ValueError:
    print ("Error: Invalid Input Please Enter A Number")