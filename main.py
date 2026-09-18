import importlib

print("--------------------------------------------------------------------")
print("Cybersecurity Log Analysis and Detection of Threats System (CLADTS)")
print("--------------------------------------------------------------------")
print("\nWelcome to CLADTS!")
print("This system will help you analyze your logs and detect potential threats.")

while True:
    print("Please select an option to input your log data and receive analysis results.")
    print("\nOptions:")
    print("""
                1. Add Log
                2. View Logs
                3. Search Logs
                4. Filter Logs
                5. Delete Log
                6. Detect Threats
                7. Generate Report
                8. Save Logs
                9. Load Logs
                10. Exit""")

    try:
        option = int(input("Enter your option (1-10): "))
    except ValueError:
        print("Invalid input. Please enter a valid number between 1 and 10.")
        continue
    #option ka range
    if option < 1 or option > 10:
        print("Invalid input. Please enter a number between 1 and 10.")
        continue
    #khtm
    if option == 10:
        print("Exiting the system. Goodbye!")
        break
#final error checking for module and function existence
    try:
        getattr(importlib.import_module(f"features.f{option}"), f"f{option}")()
    except Exception as e:
        print(f"Error: Could not find implementation file or function for option {option}.")