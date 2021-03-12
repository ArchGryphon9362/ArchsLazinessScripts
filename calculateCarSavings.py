# The Values I'll be feeding it:
# 10
# Nissan Leaf
# 29935
# 16.40
# Kia E-Niro 64kWh
# 38995
# 17.30
# Tesla Model 3 LR
# 58990
# 15.20
# Hyundai Kona 64kWh
# 41595
# 16.20
# Jaguar I-Pace
# 81925
# 23.20
# Renault Zoe ZE50 R110
# 33990
# 16.50
# Audi E-Tron GT
# 104895
# 20.20
# Volkswagen ID.3 Pro
# 35000
# 16.60
# BMW i3
# 43690
# 16.50
# Hyundai Ioniq
# 37015
# 15.30
#
# The Output:
# Nissan Leaf			50.531735313977045
# Kia E-Niro 64kWh		68.31639803784164
# Tesla Model 3 LR		94.96136509980684
# Hyundai Kona 64kWh	69.65003348961822
# Jaguar I-Pace			190.8783783783784
# Renault Zoe ZE50 R110	57.610169491525426
# Audi E-Tron GT		209.28770949720672
# Volkswagen ID.3 Pro	59.56432947583391
# BMW i3				74.05084745762711
# Hyundai Ioniq			59.8173884938591


chargingCost = 0.24
gasCost = 9.86
repeat = int(input("How Many Cars: "))
carNames = []
carCosts = []
carConsumptions = []

for i in range(repeat):
	carNames.append(input("Car Name: "))
	carCosts.append(int(input("Car's Cost: ")))
	carConsumptions.append(float(input("Car Consumption: ")))

for i in range(repeat):
	print(carNames.pop(0) + "\t" + str(carCosts.pop(0) / ((gasCost - (carConsumptions.pop(0) * chargingCost)) * 100)))