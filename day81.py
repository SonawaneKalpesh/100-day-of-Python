info_count = 0
warning_count = 0
error_count = 0

with open("log.txt", "r") as file:
    for line in file:
        line = line.strip()

        if line.startswith("INFO"):
            info_count += 1

        elif line.startswith("WARNING"):
            warning_count += 1

        elif line.startswith("ERROR"):
            error_count += 1

print("===== LOG ANALYSIS =====")
print("INFO:", info_count)
print("WARNING:", warning_count)
print("ERROR:", error_count)