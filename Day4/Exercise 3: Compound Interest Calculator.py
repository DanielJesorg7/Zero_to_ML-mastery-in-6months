principal = float(input("Principal: "))
rate_percentage = float(input("Rate (%): "))
years = int(input("Years: "))
compounds_per_year = int(input("Compounds per year: "))

r = rate_percentage / 100
final_amount = principal * (1 + r / compounds_per_year) ** (compounds_per_year * years)
total_interest = final_amount - principal

print(f"Final amount: ${final_amount:.2f}")
print(f"Total interest: ${total_interest:.2f}")
