def water_plants(plant_list):
    print("Opening watering system")
    try:
        for plant in plant_list:
            print("Watering " + plant)
        print("Watering completed successfully!\n")
    except TypeError:
        print("Error: Cannot water None - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Testing with error...")
    water_plants(["tomato", None, None])
    print("\nCleanup always happens, ever with errors!")
