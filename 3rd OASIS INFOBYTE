print("Welcome to Body Mass Index Calculator BMI")
while True:
    try:
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        if age <= 0 or age > 150:
            raise ValueError("Invalid age. Please enter a valid age.")
        break
    except ValueError as ve:
        print(ve)
print("Welcome",name)

while True:
    try:
        height = float(input("Enter the Height in cm: "))
        if height <= 0 or height > 300:
            raise ValueError("Invalid height. Please enter a valid height.")
        break
    except ValueError as ve:
        print(ve)

while True:
    try:
        weight = float(input("Enter the Weight in kg: "))
        if weight <= 0 or weight > 500:
            raise ValueError("Invalid weight. Please enter a valid weight.")
        break
    except ValueError as ve:
        print(ve)

bmi = weight / ((height / 100) ** 2)
print(f"\nHello:",name)
print("Age :",age)
print(f"Your Body Mass Index is:",bmi)
if bmi<=18.5:
    print("You are UnderWeight")
    print("Health Tips:")
    print("- Ensure you are getting enough nutrients through a balanced diet.")
    print("- Consider consulting with a healthcare professional for personalized advice.")
elif bmi <=24.9:
    print("Awesome! You are healthy")
    print("Health Tips:")
    print("- Maintain a healthy lifestyle with regular exercise and a balanced diet.")
elif bmi <=29.9:
    print("You are over weight")
    print("Health Tips:")
    print("- Focus on portion control and incorporate more fruits and vegetables into your diet.")
    print("- Increase physical activity to help with weight management.")
else :
    print("You are Obese")   
    print("Health Tips:")
    print("- Prioritize a well-balanced diet and regular exercise to support weight loss.")
    print("- Consult with a healthcare professional for personalized guidance.")
