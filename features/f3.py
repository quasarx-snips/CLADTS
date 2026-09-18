import core.log_store as log_store


def f3():
    try:
        print("--------------------------------------------------------------------")
        print("Search Logs")
        print("--------------------------------------------------------------------")

        if len(log_store.logs) == 0:
            print("No logs stored yet.")
            print("--------------------------------------------------------------------")
            return

        term = input("Enter search term: ").strip()

        if term == "":
            print("Search term cannot be empty.")
            print("--------------------------------------------------------------------")
            return

        term_lower = term.lower()
        matches = []

        for record in log_store.logs:
            if not isinstance(record, dict):
                continue
            text = (
                str(record.get("username", "")) + " " +
                str(record.get("event_type", "")) + " " +
                str(record.get("status", "")) + " " +
                str(record.get("source", "")) + " " +
                str(record.get("target", "")) + " " +
                str(record.get("description", ""))
            ).lower()
            if term_lower in text:
                matches.append(record)

        print("--------------------------------------------------------------------")
        if len(matches) == 0:
            print("No logs matched your search.")
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
        print("Something went wrong while searching logs: " + str(error))
        return