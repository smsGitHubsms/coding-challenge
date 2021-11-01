def bmicalc(a,b):
    bmi=a/(b**2)
    return bmi
weight=float(input("Enter your weight in Kg: "))
height=float(input("Enter your height in Meters: "))
print("Your BMI is: ",bmicalc(weight,height))

# or
# c=bmicalc(weight,height)
# print("Your BMI is: ",c)
