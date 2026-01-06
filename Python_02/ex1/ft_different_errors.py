def garden_operations():
    """
    Demonstrates handling of various Python exceptions. This function tests
    different error types such as ValueError, ZeroDivisionError,
    FileNotFoundError, and KeyError. It also shows how to handle multiple
    exceptions together. Each exception is caught and its message is printed
    to the console, allowing the program to continue execution.
    """
    print("=== Garden Error Types Demo ===\n")
    try:
        print("Testing ValueError...")
        int("hello")
    except ValueError as e:
        print(f"Caught ValueError: {e}\n")
    try:
        print("Testing ZeroDivisionError...")
        5 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}\n")
    try:
        print("Testing FileNotFoundError...")
        open("missing.txt")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}\n")
    try:
        print("Testing KeyError...")
        data = {"plant1": "rose"}
        print(data["missing_plant"])
    except KeyError as e:
        print(f"Caught KeyError: {e}\n")
    try:
        print("Testing multiple errors together...")
        int("hello")
        5 / 0
        open("missing.txt")
    except (ValueError, ZeroDivisionError, FileNotFoundError):
        print("Caught an error, but program continues!\n")
    print("All error types tested successfully!")
