# 🚨 CyberDefenseGenAI

A smart log monitoring and anomaly detection system with email alerts, anomaly summarization, and a real-time dashboard.

---

## 📁 Project Structure

```
CyberDefenseGenAI/
├── alerts.txt           # Detected anomalies stored here
├── dashboard.py         # Graphical dashboard using matplotlib
├── input.txt            # Input log data for summarization
├── log_parser.py        # Real-time log watcher + anomaly detection + email alerts
├── logs/                # Directory containing the logs to watch
├── main.py              # Entry point if needed (optional)
├── summarizer.py        # Summarizes logs using Hugging Face
├── summary.txt          # Output of summarizer.py
├── .env                 # Contains sensitive config like email credentials
```

---

## ✅ Features

- 🕵️ Real-time Log Monitoring
- ⚠️ Anomaly Detection (errors within 5-minute windows)
- 📧 Automated Email Alerts using Gmail SMTP
- 📁 Alerts Logging in `alerts.txt`
- 🧠 Offline Log Summarization using Hugging Face (no OpenAI costs!)
- 📊 Visual Dashboard (Matplotlib)
- 🔒 Uses `.env` for sensitive config

---

## 📦 Installation

```bash
pip install -r requirements.txt
```

(Or manually install: `matplotlib`, `transformers`, `torch`, `python-dotenv`)

---

## 🔍 Real-time Monitoring

1. Set your log file path in `log_parser.py` (default: `logs/log.txt`).
2. Set your email/SMTP credentials in `.env`:

```env
Email Address:

your_email@gmail.com

(Ensure this is the correct email address you plan to use for access.)

App Password:

your_app_password

(If you don’t have an app password, search for how to generate one for your Google account, especially for use with third-party apps or services.)
```

3. Run the monitor:

```bash
python log_parser.py
```

- It watches for `ERROR` entries.
- If two errors occur within 5 minutes → sends email + logs anomaly.

---

## 🧠 Summarization with Hugging Face (Offline, Free, Powerful)

CyberDefenseGenAI includes an **offline** and **free** text summarization feature to extract key insights from long logs or reports — no OpenAI API required!

### ✨ Powered by:

- 🤗 Hugging Face Transformers
- Pre-trained Model: [`facebook/bart-large-cnn`](https://huggingface.co/facebook/bart-large-cnn)

### 📄 How It Works

- Input: The tool reads from `input.txt` (or any file you configure).
- Output: Generates a concise summary and saves it to `summary.txt`.

### 🚀 Why This Rocks

- ✅ No API keys or internet needed
- ✅ Completely free to use
- ✅ Great for summarizing threat reports, system logs, incident data, etc.

### 🧪 Usage

Make sure you've installed the dependencies:

```bash
pip install transformers torch
```

Then run the summarizer:

```bash
python summarizer.py
```

Your summarized report will be saved as:

```
📁 summary.txt
```

---

## 📊 Dashboard

Visualize anomaly frequency with Matplotlib:

```bash
python dashboard.py
```

- Shows anomalies per hour in a bar graph
- Reads data from `alerts.txt`

---

## 🚀 Coming Soon (Ideas)

- 🛡️ Log threat categorization (e.g. "Disk Failure", "Unauthorized Login")
- 🔍 Advanced filters on dashboard (by type, date, severity)
- 🌐 Web dashboard using Flask + Chart.js
- 🗃️ Archive old alerts + purge policy

---

## Contact
MD. ASIF SARDAR: sardarasif376@gmail.com
Project Link: https://github.com/sardar211/CyberDefenseGenAI

---

## Acknowledgments
Inspired by an online cybersecurity course instructor.

---

## 📜 License
This project is licensed under the MIT License - see the LICENSE file for details.

---
