import log_store


def f5():
    try:
        logs = log_store.LOGS

        if len(logs) == 0:
            print("Nothing to delete.")
            return

        print("--------------------------------------------------------------------")
        print("Delete Log")
        print("--------------------------------------------------------------------")
        print("Stored logs: " + str(len(logs)))
        print("--------------------------------------------------------------------")
        print("ID    Timestamp            Username         Event Type")
        print("--------------------------------------------------------------------")

        for record in logs:
            try:
                log_id = record.get("log_id", "?")
                ts = record.get("timestamp", "")
                user = record.get("username", "")
                event = record.get("event_type", "")
                print(str(log_id) + "     " + str(ts) + "   " + str(user) + "   " + str(event))
            except Exception:
                print("[unreadable record]")

        print("--------------------------------------------------------------------")

        #confirmation
        while True:
            raw = input("Enter log_id to delete (or 'c' to cancel): ").strip()

            if raw.lower() == "c":
                print("Delete cancelled. No changes made.")
                return

            try:
                log_id = int(raw)
                break
            except ValueError:
                print("Please enter a valid integer log_id, or 'c' to cancel.")

        log = log_store.find_log_by_id(log_id)

        if log is None:
            print("No log found with that ID.")
            return

        print()
        print("Selected log:")
        print("--------------------------------------------------------------------")
        try:
            print(log_store.format_log(log))
        except Exception:
            print("[unreadable record]")
        print("--------------------------------------------------------------------")

        answer = input("Delete this log permanently? (y/n): ").strip()

        if answer.lower() != "y":
            print("Delete cancelled. No changes made.")
            return

        try:
            log_store.LOGS.remove(log)
        except ValueError:
            print("That log could not be removed (it may have already been deleted).")
            return

        print("Log " + str(log_id) + " deleted successfully.")
        print("--------------------------------------------------------------------")

    except KeyboardInterrupt:
        print()
        print("Operation cancelled.")
        return
    except Exception:
        print()
        print("Something went wrong while deleting the log. Returning to menu.")
        return
