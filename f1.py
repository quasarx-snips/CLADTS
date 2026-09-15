import log_store


def f1():
    try:
        print("--------------------------------------------------------------------")
        print("Add Log")
        print("--------------------------------------------------------------------")
        print("Enter the log details below.")

        #uname
        while True:
            username = input("Username: ").strip()
            if username != "":
                break
            print("Username cannot be empty. Please try again.")

        #eventtype
        print("Select Event Type:")
        for i in range(len(log_store.event_types)):
            print("  " + str(i + 1) + ". " + log_store.event_types[i])
        while True:
            event_type = input("Event Type [1-" + str(len(log_store.event_types)) + "]: ").strip()
            if event_type.isdigit():
                number = int(event_type)
                if 1 <= number <= len(log_store.event_types):
                    event_type = log_store.event_types[number - 1]
                    break
            print("Invalid Event Type. Enter a number from 1 to " + str(len(log_store.event_types)) + ".")

        #status
        print("Select Status:")
        for i in range(len(log_store.STATUSES)):
            print("  " + str(i + 1) + ". " + log_store.STATUSES[i])
        while True:
            status = input("Status [1-" + str(len(log_store.STATUSES)) + "]: ").strip()
            if status.isdigit():
                number = int(status)
                if 1 <= number <= len(log_store.STATUSES):
                    status = log_store.STATUSES[number - 1]
                    break
            print("Invalid Status. Enter a number from 1 to " + str(len(log_store.STATUSES)) + ".")

        #source
        while True:
            source = input("Source: ").strip()
            if source != "":
                break
            print("Source cannot be empty. Please try again.")

        #target
        while True:
            target = input("Target: ").strip()
            if target != "":
                break
            print("Target cannot be empty. Please try again.")

        #risklevel
        print("Select Risk Level:")
        for i in range(len(log_store.RISK_LEVELS)):
            print("  " + str(i + 1) + ". " + log_store.RISK_LEVELS[i])
        while True:
            risk_level = input("Risk Level [1-" + str(len(log_store.RISK_LEVELS)) + "]: ").strip()
            if risk_level.isdigit():
                number = int(risk_level)
                if 1 <= number <= len(log_store.RISK_LEVELS):
                    risk_level = log_store.RISK_LEVELS[number - 1]
                    break
            print("Invalid Risk Level. Enter a number from 1 to " + str(len(log_store.RISK_LEVELS)) + ".")

        #description
        description = input("Description (optional, press Enter to skip): ").strip()

        #create log
        record = log_store.make_log(
            username, event_type, status, source, target, risk_level, description
        )

        print()
        print("Log added successfully.")
        print("\tLog ID    :\t" + str(record["log_id"]))
        print("\tTimestamp :\t" + record["timestamp"])
        print("--------------------------------------------------------------------")

    except KeyboardInterrupt:
        print()
        print("Operation cancelled.")
        return
    except Exception:
        print()
        print("Something went wrong while adding the log. Returning to menu.")
        return
