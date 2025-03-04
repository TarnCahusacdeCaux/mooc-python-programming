gift_value: float = float(input("Value of gift: "))

if 5_000 <= gift_value < 25_000:
    lower_limit_tax: int = 100
    lower_limit: int = 5_000
    tax_rate: float = 0.08
    print(
        "Amount of tax: " + str(lower_limit_tax + (gift_value - lower_limit) * tax_rate)
    )
elif 25_000 <= gift_value < 55_000:
    lower_limit_tax: int = 1_700
    lower_limit: int = 25_000
    tax_rate: float = 0.1
    print(
        "Amount of tax: " + str(lower_limit_tax + (gift_value - lower_limit) * tax_rate)
    )
elif 55_000 <= gift_value < 200_000:
    lower_limit_tax: int = 4_700
    lower_limit: int = 55_000
    tax_rate: float = 0.12
    print(
        "Amount of tax: " + str(lower_limit_tax + (gift_value - lower_limit) * tax_rate)
    )
elif 200_000 <= gift_value < 1_000_000:
    lower_limit_tax: int = 22_100
    lower_limit: int = 200_000
    tax_rate: float = 0.15
    print(
        "Amount of tax: " + str(lower_limit_tax + (gift_value - lower_limit) * tax_rate)
    )
elif gift_value > 1_000_000:
    lower_limit_tax: int = 142_100
    lower_limit: int = 1_000_000
    tax_rate: float = 0.17
    print(
        "Amount of tax: " + str(lower_limit_tax + (gift_value - lower_limit) * tax_rate)
    )
else:
    print("No tax!")
