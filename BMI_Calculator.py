name = input("Enter your name: ")

weight = int(input("Enter your weight in pounds: "))

height = int(input("Enter your height in inches: "))

BMI = (weight * 703) / (height * height)

print(BMI)
#BMI = (weight in pounds x 703) / (height in inches x height in inches)

if BMI>0:
    if (BMI<18.5):
        print(name,"You are Underweight")
    elif (BMI<=24.9):
        print(name,"You are Normal Weight")
    elif (BMI<29.9):
        print(name,"You are Overweight")
    elif (BMI<34.9):
        print(name,"You are Obese")
    elif(BMI<39.9):
        print(name,"You are Morbidly Obese")
    else:
        print("Enter Valid Inputs")