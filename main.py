import re
from collections import defaultdict

# Path to the log file
log_file_path = "logs/sample.log"

# Track failed logins per IP
failed_logins = defaultdict(int)
suspicious_admin_access = defaultdict(int)

# Read the log file
with open(log_file_path, "r") as file:
    lines = file.readlines()

for line in lines:
    # Extract IP, URL, and status code using regex
    match = re.search(r'(\d+\.\d+\.\d+\.\d+).+?"(GET|POST) (.*?) HTTP/1.1" (\d+)', line)
    if match:
        ip, method, url, status = match.groups()

        # Track repeated admin access
        if "/admin" in url:
            suspicious_admin_access[ip] += 1

        # Track failed logins
        if "/login" in url and status == "401":
            failed_logins[ip] += 1

        # Detect login success after failures
        if "/login" in url and status == "200" and failed_logins[ip] >= 2:
            print(f"⚠️ Possible brute-force attack by {ip} → {failed_logins[ip]} failed attempts, then success!")

# Print summary of findings
print("\n🔎 Suspicious Admin Access Attempts:")
for ip, count in suspicious_admin_access.items():
    if count > 1:
        print(f"🔐 IP {ip} tried to access /admin {count} times.")

print("\n🔎 Repeated Failed Logins:")
for ip, count in failed_logins.items():
    if count >= 2:
        print(f"🚫 IP {ip} had {count} failed login attempts.")
