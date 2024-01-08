import psutil
import json
import csv
from datetime import datetime
import os
import matplotlib.pyplot as plt

def get_system_info():
    # Get disk usage statistics
    disk_usage = psutil.disk_usage('/')

    # Get memory usage statistics
    memory_usage = psutil.virtual_memory()

    # Extract free storage and used memory in bytes
    free_storage_bytes = disk_usage.free
    used_memory_bytes = memory_usage.used

    # Convert bytes to gigabytes for better readability
    free_storage_gb = round(free_storage_bytes / (1024 ** 3), 2)
    used_memory_gb = round(used_memory_bytes / (1024 ** 3), 2)

    return {'free_storage_gb': free_storage_gb, 'used_memory_gb': used_memory_gb}

def log_to_json(system_info):
    log_entry = {'timestamp': str(datetime.now()), **system_info}
    file_path = '/Users/paullack/Documents/projects/system_info.json'

    if os.path.exists(file_path):
        # Append to existing JSON file
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)

        data.append(log_entry)

        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=2)
    else:
        # Create a new JSON file
        with open(file_path, 'w') as json_file:
            json.dump([log_entry], json_file, indent=2)

def log_to_csv(system_info):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M')  # Format without seconds
    log_entry = [timestamp, system_info['free_storage_gb'], system_info['used_memory_gb']]
    file_path = '/Users/paullack/Documents/projects/system_info.csv'
    header = ['Timestamp', 'Free Storage (GB)', 'Used Memory (GB)']

    if os.path.exists(file_path):
        # Append to existing CSV file
        with open(file_path, 'a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            # Check if it's the first entry to write the header
            if csv_file.tell() == 0:
                csv_writer.writerow(header)
            csv_writer.writerow(log_entry)
    else:
        # Create a new CSV file
        with open(file_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(header)
            csv_writer.writerow(log_entry)

def plot_data(csv_file_path):
    timestamps = []
    free_storage_values = []

    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)  # Skip the header

        for row in csv_reader:
            timestamps.append(row[0])
            free_storage_values.append(float(row[1]))

    last_10min_free_storage_values = free_storage_values[-1440:]
    last_10min_timestamps = timestamps[-1440:]

    # Plotting
    plt.figure(figsize=(10, 10))
    plt.plot(last_10min_timestamps, last_10min_free_storage_values, label='Free Storage (GB)')
    plt.title("Paul's Laptop Available Storage")
    plt.xlabel('Last Hour Minutes')
        # Setting x-ticks every 10 minutes
    x_ticks_positions = range(0, len(last_10min_timestamps), 60)
    x_ticks_labels = [last_10min_timestamps[i] for i in x_ticks_positions]
    plt.xticks(x_ticks_positions, x_ticks_labels, rotation=-45, ha='left')
    plt.ylabel('GB')
    plt.legend()

    # Save the plot as a PNG file
    plot_file_path = '/Users/paullack/Documents/projects/system_info.png'
    plt.savefig(plot_file_path)
    plt.close()

    print(f"Plot saved to {plot_file_path}")

if __name__ == "__main__":
    system_info = get_system_info()
    log_to_json(system_info)
    log_to_csv(system_info)

    print(f"Free storage: {system_info['free_storage_gb']} GB")
    print(f"Used memory: {system_info['used_memory_gb']} GB")
    print("Logs saved to system_info.json and system_info.csv")

    # Plot data and save as PNG
    csv_file_path = '/Users/paullack/Documents/projects/system_info.csv'  # Adjust if needed
    plot_data(csv_file_path)