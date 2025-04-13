def calculate_bmi(weight_kg, height_cm):
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)

weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (cm): "))
bmi = calculate_bmi(weight, height)
print("BMI:", bmi)

if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 24.9:
    print("Normal")
elif 25 <= bmi < 29.9:
    print("Overweight")
else:
    print("Obese")
