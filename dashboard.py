import matplotlib.pyplot as plt
from datetime import datetime
import re
from collections import Counter, defaultdict

# Function to parse anomaly timestamps from alerts.txt
def parse_anomalies(file_path):
    timestamps = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                match = re.findall(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', line)
                if match:
                    for ts in match:
                        timestamps.append(datetime.strptime(ts, "%Y-%m-%d %H:%M:%S"))
    except FileNotFoundError:
        print("🚫 alerts.txt not found.")
    return timestamps

# Function to group anomalies per hour
def group_by_hour(timestamps):
    hourly = Counter()
    for ts in timestamps:
        hour_key = ts.strftime("%Y-%m-%d %H:00")
        hourly[hour_key] += 1
    return hourly

# Main
anomalies = parse_anomalies("alerts.txt")

if not anomalies:
    print("⚠️ No data to display on the dashboard.")
else:
    hourly_counts = group_by_hour(anomalies)

    # Sort by time for display
    sorted_hours = sorted(hourly_counts.items())

    x = [item[0] for item in sorted_hours]
    y = [item[1] for item in sorted_hours]

    plt.figure(figsize=(12, 6))
    bars = plt.bar(x, y, color="#FF5733", edgecolor="black")
    plt.xticks(rotation=45, ha='right')
    plt.title("📊 Anomalies Detected Per Hour")
    plt.xlabel("Hour")
    plt.ylabel("Number of Anomalies")
    plt.tight_layout()

    # Add value labels to bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height + 0.1, f'{height}', ha='center', fontsize=9)

    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
