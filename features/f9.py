import json

import core.log_store as log_store


def f9():
    try:
        path = log_store.SAVE_FILE

        #open and read the file
        try:
            file = open(path, "r", encoding="utf-8")
            try:
                data = json.load(file)
            finally:
                file.close()
        except FileNotFoundError:
            print("No saved data file found yet.")
            return
        except json.JSONDecodeError:
            print("The saved file is corrupted and cannot be read.")
            return
        except OSError:
            print("Could not open the saved file.")
            return

        #type check
        if not isinstance(data, list):
            print("The saved file has an unexpected format.")
            return

        #empty list check
        if len(data) == 0:
            print("The saved file contains no logs.")
            return

        #validation
        valid_records = []
        skipped = 0
        for record in data:
            try:
                if log_store.is_valid_log(record):
                    valid_records.append(record)
                else:
                    skipped = skipped + 1
            except Exception:
                skipped = skipped + 1

        #memory replacement warning
        print("Warning: current in-memory logs will be replaced with the saved file contents.")

        log_store.logs.clear()
        log_store.logs.extend(valid_records)

        #report results
        print("Loaded " + str(len(valid_records)) + " record(s) from " + path + ".")
        print("Skipped " + str(skipped) + " invalid record(s).")
        print("Total logs now in memory: " + str(len(log_store.LOGS)) + ".")

    except KeyboardInterrupt:
        print()
        print("Operation cancelled.")
        return
    except Exception:
        print()
        print("Something went wrong while loading. Returning to menu.")
        return
