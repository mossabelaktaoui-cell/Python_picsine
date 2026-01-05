"""This function take the harvest of 3 days,
then print the total harvest"""


def ft_harvest_total():
    total = 0
    i = 1
    while i < 4:
        total += int(input(f"Day {i} harvest: "))
        i += 1
    print(f"Total harvest: {total}")
