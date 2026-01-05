"""This function take last watering time,
and tell you is the plant need water or not"""


def ft_water_reminder():
    days = int(input("Days since last watering: "))
    if days <= 2:
        print("Plants are fine")
    else:
        print("Water the plants!")
