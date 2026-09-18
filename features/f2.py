import core.log_store as log_store


def f2():
    try:
        logs = log_store.LOGS

        if not logs:
            print("No logs stored yet.")
            return

        total = len(logs)
        print("\t--------------------------------------------------------------------")
        print(f"\tStored Logs (total: {total})")
        print("\t--------------------------------------------------------------------")

        divider = "\t--------------------------------------------------------------------"
        for index, record in enumerate(logs, start=1):
            print()
            print(f"Entry #{index}")
            print(divider)
            try:
                print(log_store.format_log(record))
            except Exception:
                print("[unreadable record]")
            print(divider)

        print()
        print(f"\tEnd of listing. {total} log(s) shown.")
        print("--------------------------------------------------------------------")

        try:
            input("Press Enter to return to the menu...")
        except KeyboardInterrupt:
            print()
            print("Operation cancelled.")
            return

    except KeyboardInterrupt:
        print()
        print("Operation cancelled.")
        return
    except Exception:
        print()
        print("Something went wrong while viewing logs. Returning to menu.")
        return
