import core.log_store as log_store


def f7():
    try:
        print("--------------------------------------------------------------------")
        print("Security Analysis Report")
        print("--------------------------------------------------------------------")

        if len(log_store.logs) == 0:
            print("No logs stored yet. Cannot generate a report.")
            print("--------------------------------------------------------------------")
            return

        total = len(log_store.logs)
        print("Total Logs : " + str(total))

        # --- Risk distribution ---
        risk_count = {}
        for level in log_store.risk_levels:
            risk_count[level] = 0
        for record in log_store.logs:
            if not isinstance(record, dict):
                continue
            level = record.get("risk_level", "Unknown")
            if level in risk_count:
                risk_count[level] += 1

        print()
        print("Risk Distribution:")
        for level in log_store.risk_levels:
            print("  " + level + " : " + str(risk_count.get(level, 0)))

        # --- Status distribution ---
        status_count = {}
        for status in log_store.statuses:
            status_count[status] = 0
        for record in log_store.logs:
            if not isinstance(record, dict):
                continue
            status = record.get("status", "Unknown")
            if status in status_count:
                status_count[status] += 1

        print()
        print("Status Distribution:")
        for status in log_store.statuses:
            print("  " + status + " : " + str(status_count.get(status, 0)))

        # --- Login statistics ---
        login_total = 0
        login_success = 0
        login_failure = 0
        for record in log_store.logs:
            if not isinstance(record, dict):
                continue
            if record.get("event_type") == "Login Success":
                login_total += 1
                login_success += 1
            elif record.get("event_type") == "Login Failure":
                login_total += 1
                login_failure += 1

        print()
        print("Login Statistics:")
        print("  Total   : " + str(login_total))
        print("  Success : " + str(login_success))
        print("  Failure : " + str(login_failure))

        # --- Top users ---
        user_count = {}
        for record in log_store.logs:
            if not isinstance(record, dict):
                continue
            user = record.get("username", "unknown")
            user_count[user] = user_count.get(user, 0) + 1

        sorted_users = sorted(user_count.items(), key=lambda item: item[1], reverse=True)

        print()
        print("Top Users:")
        count = 0
        for user, number in sorted_users:
            if count >= 5:
                break
            print("  " + str(user) + " : " + str(number))
            count += 1

        # --- High risk count ---
        high_count = 0
        for record in log_store.logs:
            if not isinstance(record, dict):
                continue
            if record.get("risk_level") == "High":
                high_count += 1

        print()
        print("High Risk Events : " + str(high_count))
        print("--------------------------------------------------------------------")

        # --- Save report ---
        answer = input("Save this report to a file? (y/n): ").strip().lower()
        if answer == "y":
            path = "security_report.txt"
            try:
                f = open(path, "w", encoding="utf-8")
                f.write("Security Analysis Report\n")
                f.write("------------------------\n")
                f.write("Total Logs : " + str(total) + "\n\n")
                f.write("Risk Distribution:\n")
                for level in log_store.risk_levels:
                    f.write("  " + level + " : " + str(risk_count.get(level, 0)) + "\n")
                f.write("\nStatus Distribution:\n")
                for status in log_store.statuses:
                    f.write("  " + status + " : " + str(status_count.get(status, 0)) + "\n")
                f.write("\nLogin Statistics:\n")
                f.write("  Total   : " + str(login_total) + "\n")
                f.write("  Success : " + str(login_success) + "\n")
                f.write("  Failure : " + str(login_failure) + "\n")
                f.write("\nTop Users:\n")
                count = 0
                for user, number in sorted_users:
                    if count >= 5:
                        break
                    f.write("  " + str(user) + " : " + str(number) + "\n")
                    count += 1
                f.write("\nHigh Risk Events : " + str(high_count) + "\n")
                f.close()
                print("Report saved to " + path + ".")
            except (OSError, TypeError) as error:
                print("Could not save report: " + str(error))
        else:
            print("Report not saved.")

        print("--------------------------------------------------------------------")
        input("Press Enter to return to the menu...")

    except KeyboardInterrupt:
        print()
        print("Operation cancelled.")
        return
    except Exception as error:
        print()
        print("Something went wrong while generating the report: " + str(error))
        return