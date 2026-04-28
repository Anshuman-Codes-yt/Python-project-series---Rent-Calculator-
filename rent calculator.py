food = int(input("Enter your food expence of this month: "))
water = int(input("Enter the water expence of the month: "))
home_rent = int(input("Enter the rent of this month: "))
electricity = int(input("Enter the electricity expence of the month: "))
paid_subscriptions = int(input("Enter the paid subscriptions expence of the month: "))
shoping = int(input("Enter the shoping expence of the month:"))
other = int(input("Enter all other expences in the month: "))

persons = int(input("Enter the number person living the group: "))

rent = ((food + water + home_rent + electricity + paid_subscriptions + shoping + other) / persons)

print(f"The number of amount each person have to pay is {rent}")