def calculate_bmi():
    print("===== BMI Calculator =====")
    print()

    # Taking input with validation
    while True:
        try:
            weight = float(input("Enter your weight in kg: "))
            height = float(input("Enter your height in meters (ex: 1.65): "))
            
            if weight <= 0 or height <= 0:
                print("Error: Weight and height must be greater than 0. Please try again.\n")
                continue
            break
        except ValueError:
            print("Error: Please enter numbers only. Try again.\n")

    # Formula: BMI = weight / (height^2)
    bmi = weight / (height * height)
    bmi_rounded = round(bmi, 2)

    # Classification as per standard categories
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal (18.5 - 24.9)"
    elif bmi < 30:
        category = "Overweight (25 - 29.9)"
    else:
        category = "Obese (>= 30)"

    # Displaying result
    print()
    print(f"Your BMI is: {bmi_rounded}")
    print(f"You are in: {category} category")

# Run the program
calculate_bmi()
