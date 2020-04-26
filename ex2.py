num1=int(input("enter a number "))
if num1%4==0:
    print(num1,"is multiple of 4")
elif num1%2==0:
    print(num1,"is an even")
else:
    print(num1,"is an odd")
num2=int(input("divided number is "))
if num1%num2==0:
    print("it divides evenly into num is", num2)
else:
    print("it does not divides the number", num2)
