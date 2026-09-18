import core.log_store as log_store


def pick_event_type():
    print("Select Event Type filter:")
    print(" 0. All")
    for i in range(len(log_store.event_types)):
        print(" " + str(i + 1) + ". " + log_store.event_types[i])
    while True:
        raw = input("Enter choice [0-" + str(len(log_store.event_types)) + "]: ").strip()
        if raw.isdigit():
            number = int(raw)
            if 0 <= number <= len(log_store.event_types):
                if number == 0:
                    return None
                return log_store.event_types[number - 1]
        print("Invalid choice. Try again.")


def pick_risk_level():
    print("Select Risk Level filter:")
    print(" 0. All")
    for i in range(len(log_store.risk_levels)):
        print(" " + str(i + 1) + ". " + log_store.risk_levels[i])
    while True:
        raw = input("Enter choice [0-" + str(len(log_store.risk_levels)) + "]: ").strip()
        if raw.isdigit():
            number = int(raw)
            if 0 <= number <= len(log_store.risk_levels):
                if number == 0:
                    return None
                return log_store.risk_levels[number - 1]
        print("Invalid choice. Try again.")


def f4():
    try:
        print("--------------------------------------------------------------------")
        print("Filter Logs")
        print("--------------------------------------------------------------------")

        if len(log_store.logs) == 0:
            print("No logs stored yet.")
            print("--------------------------------------------------------------------")
            return

        event_filter = pick_event_type()
        risk_filter = pick_risk_level()

        matches = []
        for record in log_store.logs:
            if not isinstance(record, dict):
                continue
            if event_filter is not None and record.get("event_type") != event_filter:
                continue
            if risk_filter is not None and record.get("risk_level") != risk_filter:
                continue
            matches.append(record)

        print("--------------------------------------------------------------------")
        if len(matches) == 0:
            print("No logs matched the selected filters.")
        else:
            print("Found " + str(len(matches)) + " matching log(s):")
            print("--------------------------------------------------------------------")
            for record in matches:
                print(log_store.format_log(record))
                print("--------------------------------------------------------------------")

        input("Press Enter to return to the menu...")

    except KeyboardInterrupt:
        print()
        print("Operation cancelled.")
        return
    except Exception as error:
        print()
        print("Something went wrong while filtering logs: " + str(error))
        return