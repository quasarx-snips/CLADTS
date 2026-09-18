import json

import core.log_store as log_store


def f8():
    try:
        path = log_store.SAVE_FILE
        count = len(log_store.LOGS)

        try:
            file = open(path, "w", encoding="utf-8")
            try:
                json.dump(log_store.LOGS, file, indent=2)
            finally:
                file.close()
        except (OSError, TypeError, ValueError) as error:
            print("Could not save the file.")
            print("Reason: " + str(error))
            return

        if count == 0:
            print("Note: no logs were in memory. An empty list was saved.")

        print("--------------------------------------------------------------------")
        print("Saved " + str(count) + " log record(s) to " + path + ".")

    except KeyboardInterrupt:
        print()
        print("Operation cancelled.")
        return
    except Exception:
        print()
        print("Something went wrong while saving. Returning to menu.")
        return
