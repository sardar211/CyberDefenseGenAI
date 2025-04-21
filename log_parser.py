import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import os

# Function to send an email notification
def send_email(subject, message):
    try:
        sender_email = "sardarasif376@gmail.com"
        receiver_email = "asifr6867@gmail.com"
        password = "izvo juoc tzlh pkld"

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            text = msg.as_string()
            server.sendmail(sender_email, receiver_email, text)
            print(f"📧 Email sent to {receiver_email}")

    except Exception as e:
        print(f"❌ Error sending email: {e}")
        
# Function to save anomalies to a file
def log_anomaly_to_file(message):
    try:
        with open("alerts.txt", "a") as file:
            file.write(f"{message}\n")
        print("📝 Anomaly saved to alerts.txt")
    except Exception as e:
        print(f"❌ Error writing to alerts.txt: {e}")

# Function to detect anomalies based on time difference
def detect_anomalies(log_list, log_type):
    if len(log_list) < 2:
        return

    for i in range(1, len(log_list)):
        time_diff = log_list[i] - log_list[i - 1]
        if time_diff < datetime.timedelta(minutes=5):
            alert_message = f"[ALERT] {log_type} anomaly detected: {log_list[i - 1]} and {log_list[i]} occurred within 5 minutes."
            print(alert_message)
            send_email(f"{log_type} Anomaly Detected", alert_message)
            log_anomaly_to_file(alert_message)  # 💾 Save to alerts.txt
# Function to parse logs and detect anomalies
def parse_logs(logs):
    errors = []
    warnings = []
    info = []

    for log in logs:
        log = log.strip()
        if not log or not log.startswith('['):
            continue  # Skip empty or malformed lines

        try:
            timestamp_str = log.split("]")[0][1:]
            timestamp = datetime.datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')

            if 'ERROR' in log:
                errors.append(timestamp)
                print(f"❗ ERROR found: {log}")
            elif 'WARNING' in log:
                warnings.append(timestamp)
                print(f"⚠️ WARNING found: {log}")
            elif 'INFO' in log:
                info.append(timestamp)
                print(f"ℹ️ INFO found: {log}")
            else:
                print(f"❓ Uncategorized log: {log}")

        except Exception as e:
            print(f"🚫 Error parsing log: {e}")

    detect_anomalies(errors, 'ERROR')
    detect_anomalies(warnings, 'WARNING')

# Real-time log monitoring function
def monitor_log_file(file_path):
    print("👀 Watching log file in real-time... (Press Ctrl+C to stop)")
    last_position = 0

    try:
        while True:
            if not os.path.exists(file_path):
                print("❌ Log file not found.")
                break

            with open(file_path, 'r') as file:
                file.seek(last_position)
                new_lines = file.readlines()
                if new_lines:
                    parse_logs(new_lines)
                    last_position = file.tell()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 Stopped monitoring.")

# Start real-time monitoring
monitor_log_file('input.txt')
