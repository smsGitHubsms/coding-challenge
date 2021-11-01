def divide(a,b):
      try:
        return a/b
      except ZeroDivisionError:
        print("Divide by zero is not possible")

num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))
print("The division value is: ",divide(num1,num2))

