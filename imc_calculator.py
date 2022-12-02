# IMC Calculator
name = input("What's your name? ")
weight = input("What's your weight in kilogram(Kg)? ")
height = input("What's your height in meters(m)? ")

weight_float = float(weight)
height_float = float(height)

imc = (weight_float / (height_float*height_float))

print(f"Hello, {name}. Your IMC is {imc:.2f}")

thinness = 18.5
normal = 24.9
overweight = 29.9
obesity = 39.9
severe_obesity = 40

if(imc <= thinness):
    print(f"{name} your classification is Thinness because your IMC are bellow or same that 18.5. Level 0 for obesity.")
elif (imc <= normal):
    print(f"{name} your classification is Normal because your IMC are between 18.5 and 24.9. Level 0 for obesity.")
elif (imc <= overweight):
    print(f"{name} your classification is Overweight because your IMC are between 25 and 29.9. Level 1 for obesity.")
elif (imc <= obesity):
    print(f"{name} your classification is Obesity because your IMC are between 30 and 39.9. Level 2 for obesity. We recommend seeing a doctor.")
else:
    print(f"{name} your classification is Obesity because your IMC are above 40. Level 3 for obesity. We recommend seeing a doctor.")

print("Thank you for test my app.")
