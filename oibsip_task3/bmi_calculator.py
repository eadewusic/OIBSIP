# BMI = (weight in pounds-lbs x 703) / (height in inches x height in inches)
# if you're using weight in kilograms and height in meters, there's no need to multiply by 703

def get_user_input(prompt, input_type=float):
    while True:
        try:
            value = input_type(input(prompt))
            if value <= 0:
                raise ValueError
            return value
        except ValueError:
            print("Invalid input. Please enter a positive number.")

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def classify_bmi(bmi):
    if bmi < 16.0:
        return "underweight (Severe Thinness)"
    elif 16.0 <= bmi < 17.0:
        return "underweight (Moderate Thinness)"
    elif 17.0 <= bmi < 18.5:
        return "underweight (Mild Thinness)"
    elif 18.5 <= bmi < 25.0:
        return "Normal weight"
    elif 25.0 <= bmi < 30.0:
        return "Overweight (Pre-obese)"
    elif 30.0 <= bmi < 35.0:
        return "Obesity (Class I)"
    elif 35.0 <= bmi < 40.0:
        return "Obesity (Class II)"
    else:
        return "Obesity (Class III)"

def main():
    print("Welcome to the BMI Calculator")

    while True:
        name = input("What is your name? ")
        print(f"Hello, {name}")
        
        weight = get_user_input("Enter your weight in kilograms: ")
        height = get_user_input("Enter your height in meters: ")
        
        bmi = calculate_bmi(weight, height)
        bmi_category = classify_bmi(bmi)
        
        print(f"Your BMI is: {bmi:.2f}")
        print(f"Dear {name}, you are classified as '{bmi_category}'")
        
        while True:
            exit_prompt = input("Do you want to calculate another BMI? (yes/no): ").strip().lower()
            if exit_prompt in ('yes', 'no'):
                break
            print("Invalid input. Please enter 'yes' or 'no'.")
        
        if exit_prompt == 'no':
            print("Thank you for using the BMI Calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()
