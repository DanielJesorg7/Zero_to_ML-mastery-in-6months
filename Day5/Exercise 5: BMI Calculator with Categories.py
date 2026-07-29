weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height**2)
bmi_rounded = round(bmi, 1)

if bmi_rounded < 18.5:
    category = "Underweight"
    advice = "Consider speaking with a doctor or dietitian to ensure balanced nutrition."
elif 18.5 <= bmi_rounded <= 24.9:
    category = "Normal weight"
    advice = "Great job! Keep maintaining a balanced diet and regular physical activity."
elif 25.0 <= bmi_rounded <= 29.9:
    category = "Overweight"
    advice = "Incorporating more nutrient-dense meals and daily exercise can support regular wellness."
elif 30.0 <= bmi_rounded <= 34.9:
    category = "Obese Class I"
    advice = "Small, consistent lifestyle modifications can significantly benefit your health."
elif 35.0 <= bmi_rounded <= 39.9:
    category = "Obese Class II"
    advice = "Consulting a healthcare specialist can provide tailored strategies for your wellbeing."
else:  
    category = "Obese Class III"
    advice = "It is highly recommended to seek professional guidance for a comprehensive health plan."

print(f"\nBMI: {bmi_rounded}")
print(f"Category: {category}")
print(f"Health Advice: {advice}")
