def ft_water_reminder():
    date = int(input("Days since last watering: "))
    if date > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
