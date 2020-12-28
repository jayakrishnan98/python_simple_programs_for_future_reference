sales = int(input("Enter the sales-"))
basic = 4000
conveyance = 500
da = 1.1 * basic
if sales >= 100000:
    hra = 0.2 * basic
    incentive = 0.1 * sales
    bonus = 1000
else:
    hra = 0.1 * basic
    incentive = 0.4 * sales
    bonus = 5000

salary = basic + hra + da + conveyance + incentive + bonus
print(f"Salary of Sales executive;{salary}")

