price = []
for _ in range(5):
    price.append(int(input()))
hamburgur = price[0:3]
beverage = price[3:5]

print(min(hamburgur) + min(beverage) - 50)