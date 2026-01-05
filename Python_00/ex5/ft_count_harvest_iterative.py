"""This function take the remainig time to harvest,
then reminde you at harvest day"""


def ft_count_harvest_iterative():
    day = int(input("Days until harvest: "))
    i = 1
    while i <= day:
        print(f"Day {i}")
        i += 1
    print("Harvest time!")
