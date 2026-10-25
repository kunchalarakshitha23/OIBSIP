# BMI Calculator - Python Task 2

## About
Oasis Infobyte Task 2 - BMI Calculator in Python

## Code Logic
```python
weight = float(input("Weight in kg: "))
height = float(input("Height in meters: "))
bmi = weight / (height * height)
print(f"Your BMI is: {bmi}")

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")
