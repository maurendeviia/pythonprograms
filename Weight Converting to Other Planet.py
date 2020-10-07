mass = input("Input mass of things (Kg)\n")
#Choose Planet
planet = input ("Mercury,Venus,Earth,Mars,Jupiter,Saturn,Uranus, or Neptune\n")
#Algorithm
if planet.lower() == "Mercury".lower():
    weight = int(mass) * 3.7
    print("Weight in planet Mercury is ",weight, "Newton")
elif planet.lower() == "Venus".lower():
    weight = int(mass) * 8.87
    print("Weight in planet Venus is ",weight, "Newton")
elif planet.lower() == "Earth".lower():
    weight = int(mass) * 9.807
    print("Weight in planet Earth is ",weight, "Newton")
elif planet.lower() == "Mars".lower():
    weight = int(mass) * 3.711
    print("Weight in planet Mars is ",weight, "Newton")
elif planet.lower() == "Jupiter".lower():
    weight = int(mass) * 24,79
    print("Weight in planet Jupiter is ",weight, "Newton")
elif planet.lower() == "Saturn".lower():
    weight = int(mass) * 10.44
    print("Weight in planet Saturn is ",weight, "Newton")
elif planet.lower() == "Urannus".lower():
    weight = int(mass) * 8.69
    print("Weight in planet Uranus is ",weight, "Newton")
elif planet.lower() == "Neptune".lower():
    weight = int(mass) * 11.15
    print("Weight in planet Neptune is ",weight, "Newton")
else:
    print("Typo!!!") #If Typo
