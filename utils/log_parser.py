import pandas as pd
import re
import os

def parse_logs(filepath):
    suspicious_entries = []
    
    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            match = re.search(r"Failed password for (invalid user )?(\w+) from ([\d\.]+) port", line)
            if match:
                username = match.group(2)
                ip_address = match.group(3)
                suspicious_entries.append({"Username": username, "IP Address": ip_address, "Log Entry": line.strip()})

    # Convert to DataFrame
    df = pd.DataFrame(suspicious_entries)

    # Save result
    result_filename = f"result_{os.path.basename(filepath)}.csv"
    result_path = os.path.join("results", result_filename)
    df.to_csv(result_path, index=False)
    
    return result_filename
