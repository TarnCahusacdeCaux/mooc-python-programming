wage: float = float(input("Hourly wage: "))
hours_worked: float = float(input("Hours worked: "))
day: str = str(input("Day of the week: "))

daily_wages: float = wage * hours_worked

if day.lower() == "sunday":
    print(f"Daily wages: {daily_wages * 2} euros")
else:
    print(f"Daily wages: {daily_wages} euros")
