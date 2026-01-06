def check_plant_health(plant_name, water_level, sunlight_hours):
    """Validate plant health based on name, water level, and sunlight hours."""
    if plant_name == "":
        raise ValueError("Error: Plant name cannot be empty!")
    if water_level < 1 or water_level > 10:
        raise ValueError(f"Error: Water level {water_level} "
                         "is too high (max 10)")
    if sunlight_hours < 2 or sunlight_hours > 12:
        raise ValueError("Error: Sunlight hours 0 is too low (min 2)")
    print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks():
    """Run tests for the `check_plant_health` function."""
    print("=== Garden Plant Health Checker ===")
    print("\nTesting good values...")
    try:
        check_plant_health("tomato", 5, 8)
    except ValueError as e:
        print(e)
    print("\nTesting empty plant name...")
    try:
        check_plant_health("", 5, 8)
    except ValueError as e:
        print(e)
    print("\nTesting bad water level...")
    try:
        check_plant_health("tomato", 15, 8)
    except ValueError as e:
        print(e)
    print("\nTesting bad sunlight hours...")
    try:
        check_plant_health("tomato", 5, 0)
    except ValueError as e:
        print(e)
    print("\nAll error raising tests completed!")
