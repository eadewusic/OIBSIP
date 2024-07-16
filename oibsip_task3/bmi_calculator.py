# BMI = (weight in pounds-lbs x 703) / (height in inches x height in inches)

name = input("What is your name? ")
print("Welcome to the BMI Calculator,",name)
weight = int(input("Enter your weight in kilograms: "))
height = int(input("Enter your height in metres: "))
BMI = (weight * 703) / (height * height)
 
print("Your BMI is:",BMI)

if BMI>0:
    if (BMI<16.0):
        print("Dear", name +", you are classified as 'underweight (Severe Thinness)'")

    if (BMI<=16.9):
        print("Dear", name +", you are classified as 'underweight (Moderate Thinness)'")

    if (BMI<=18.4):
        print("Dear", name +", you are classified as 'underweight (Mild Thinness)'")

    elif (BMI<=24.9):
        print("Dear", name +", you are classified as 'Normal weight'")

    elif (BMI<=29.9):
        print("Dear", name +", you are classified as 'Overweight (Pre-obese)'")

    elif (BMI<=34.9):
        print("Dear", name +", you are classified as 'Obesity (Class I)'")

    elif (BMI<=39.9):
        print("Dear", name +", you are classified as 'Obesity (Class II)'")

    else:
        print("Dear", name +", you are classified as 'Obesity (Class III)'")

else:
    print("Enter a valid input")