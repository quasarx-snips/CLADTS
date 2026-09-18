import core.log_store as log_store


def f6():
    try:
        print("--------------------------------------------------------------------")
        print("Threat Detection")
        print("--------------------------------------------------------------------")

        if len(log_store.logs) == 0:
            print("No logs stored yet.")
            print("--------------------------------------------------------------------")
            return

        # --- Failed login counts ---
        failed_counts = {}
        for record in log_store.logs:
            if not isinstance(record, dict):
                continue
            if record.get("event_type") == "Login Failure":
                user = record.get("username", "unknown")
                failed_counts[user] = failed_counts.get(user, 0) + 1

        print("Failed Login Counts:")
        if len(failed_counts) == 0:
            print("  None")
        else:
            for user in failed_counts:
                print("  " + str(user) + " : " + str(failed_counts[user]))
        print()

        # --- Suspicious users (more than 3 failed logins) ---
        suspicious = []
        for user in failed_counts:
            if failed_counts[user] > 3:
                suspicious.append(user)

        print("Suspicious Users (more than 3 failed logins):")
        if len(suspicious) == 0:
            print("  None")
        else:
            for user in suspicious:
                print("  " + str(user))
        print()

        # --- Sensitive file access ---
        sensitive_words = ["password", "secret", "config", "key", "admin"]
        sensitive_hits = []
        for record in log_store.logs:
            if not isinstance(record, dict):
                continue
            if record.get("event_type") == "File Access":
                target = str(record.get("target", "")).lower()
                for word in sensitive_words:
                    if word in target:
                        sensitive_hits.append(record)
                        break

        print("Sensitive File Access:")
        if len(sensitive_hits) == 0:
            print("  None")
        else:
            for record in sensitive_hits:
                print("  Log ID " + str(record.get("log_id")) +
                      " - " + str(record.get("username")) +
                      " accessed " + str(record.get("target")))
        print()

        # --- High risk events ---
        print("High Risk Events:")
        found_high = False
        for record in log_store.logs:
            if not isinstance(record, dict):
                continue
            if record.get("risk_level") == "High":
                found_high = True
                print("  Log ID " + str(record.get("log_id")) +
                      " - " + str(record.get("event_type")) +
                      " - " + str(record.get("username")))
        if not found_high:
            print("  None")

        print("--------------------------------------------------------------------")
        input("Press Enter to return to the menu...")

    except KeyboardInterrupt:
        print()
        print("Operation cancelled.")
        return
    except Exception as error:
        print()
        print("Something went wrong during threat detection: " + str(error))
        return