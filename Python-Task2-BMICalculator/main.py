
def calculate_bmi():
    print("===== BMI Calculator =====")
    print()

    # Take input with validation
    while True:
        try:
            weight = float(input("Enter your weight in kg: "))
            height = float(input("Enter your height in meters (e.g., 1.65): "))

            if weight <= 0 or height <= 0:
                print("Error: Weight and height must be greater than 0. Please try again.\n")
                continue

            break

        except ValueError:
            print("Error: Please enter numbers only. Try again.\n")

    # Calculate BMI
    bmi = weight / (height * height)
    bmi_rounded = round(bmi, 2)

    # Classify BMI
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal (18.5 - 24.9)"
    elif bmi < 30:
        category = "Overweight (25 - 29.9)"
    else:
        category = "Obese (30 or above)"

    # Display results
    print()
    print(f"Your BMI is: {bmi_rounded}")
    print(f"Category: {category}")


# Run the program
if __name__ == "__main__":
    calculate_bmi()

