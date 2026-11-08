import csv

# PPSM record keys in the order they will appear in the CSV
PPSM_COLUMNS = [
    "ports",
    "protocol",
    "service",
    "source_ip",
    "source_name",
    "destination_ip",
    "destination_name",
]

# Column names written in the first row of the CSV
CSV_HEADERS = [
    "Ports",
    "Protocol",
    "Service",
    "Source IP",
    "Source Name",
    "Destination IP",
    "Destination Name",
]


def export_to_csv(records, file_path):
    rows = []

    # Check each record and build its CSV row
    for number, record in enumerate(records, start=1):
        if not isinstance(record, dict):
            raise TypeError(f"record {number} must be a mapping")

        # Accept either "ports" or "port" from the parser
        port_key = "ports" if "ports" in record else "port"

        # Find any required fields that are missing
        missing = [field for field in PPSM_COLUMNS[1:] if field not in record]

        if port_key not in record:
            missing.insert(0, "ports")

        if missing:
            raise ValueError(
                f"record {number} is missing required field(s): {', '.join(missing)}"
            )

        # Add the values in the same order as the column names
        row = [record[port_key]]
        for field in PPSM_COLUMNS[1:]:
            row.append(record[field])
        rows.append(row)

    # Write the header first, followed by all record rows
    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(CSV_HEADERS)
        writer.writerows(rows)

    return file_path
