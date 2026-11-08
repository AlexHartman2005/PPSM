# Entry point for the PPSM tool.
# This is where you prompt the user for input and call the appropriate functions from the other files.

# The helper functions:
from ppsm.scanner import run_scan
from ppsm.parser import parse_scan
from ppsm.export import export_to_csv


def main():

    # get input for user, we need IP and an optional name for the user to remember what they scanned.
    target = input("Enter the IP or hostname to scan: ").strip()
    if not target:
        print("No target given.")
        return
    name = input("Enter a name for the target (optional): ").strip() or None
    print(f"Scanning {target}...")
    print("This may take a while depending on the target and network conditions. Be patient.")
    
    # We just run the three functions in order to run now:

    # Scan
    xml_file = run_scan(target)

    # Parse
    records = parse_scan(xml_file, target, name)
    if not records:
        print("No open ports found :(")
        return
    
    # Export
    csv_file = export_to_csv(records, "ppsm.csv")
    print(f"Saved {len(records)} record(s) to {csv_file}")
 
 
if __name__ == "__main__":
    main()