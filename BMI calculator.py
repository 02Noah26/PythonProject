

weight = int(input("enter your weight : "))
height = float(input("enter your height here : "))
BMI =round(weight /(height*height))
print(BMI)
if BMI > 0:
    if BMI <16 :
        print("Severe thinness")
if BMI > 16:
    if BMI <17:
        print("Moderate thinness")

if BMI > 17:
    if BMI <18.5 :
        print("Mild thinness")

elif BMI > 18.5:
    if BMI <25 :
        print("Normal")

elif BMI > 25:
    if BMI <30 :
        print("Overweight")

elif BMI > 30:
    if BMI <35 :
        print("Obese Class I")

elif BMI > 35:
    if BMI <40 :
        print("Obese Class II")

elif BMI > 40:
    print("Obese Class III")

else :
    print("enter valid input")

