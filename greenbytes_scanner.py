import os
import datetime

# Main function to scan a folder for old/large files
def clean_my_storage(folder_path):
    print("--- STARTING STORAGE AUDIT ---")
    print("Scanning folder:", folder_path)
    
    if not os.path.exists(folder_path):
        print("Folder not found.")
        return

    total_files = 0
    old_files_count = 0
    wasted_bytes = 0
    
    # Loop through all files in the folder
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            total_files += 1
            full_path = os.path.join(root, file)
            
            try:
                # Check file size and age
                size = os.path.getsize(full_path)
                modified_time = os.path.getmtime(full_path)
                age_in_days = (datetime.datetime.now() - datetime.datetime.fromtimestamp(modified_time)).days
                
                # Flag if file is older than 6 months or a temporary log file
                if age_in_days > 180 or file.endswith('.log') or file.endswith('.tmp'):
                    old_files_count += 1
                    wasted_bytes += size
                    print(f"Flagged: {file} ({age_in_days} days old, Size: {size / (1024*1024):.2f} MB)")
            except:
                continue

    # Sustainability Math
    wasted_gb = wasted_bytes / (1024 * 1024 * 1024)
    power_saved = wasted_gb * 5  # 5 kWh per GB per year
    carbon_saved = power_saved * 0.4  # 0.4 kg CO2 per kWh

    print("\n--- RESULTS ---")
    print("Total Files Checked:", total_files)
    print("Unused/Old Files Found:", old_files_count)
    print("Space That Can Be Cleared:", round(wasted_gb, 4), "GB")
    print("Potential Energy Saved:", round(power_saved, 2), "kWh/Year")
    print("Potential Carbon Reduced:", round(carbon_saved, 2), "kg CO2 (Supports SDG 13)")

# Test it on the system Downloads folder
path_to_scan = os.path.expanduser("~/Downloads")
clean_my_storage(path_to_scan)