# 🔍 Enhanced Python Port Scanner

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://www.python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An enhanced port scanner written in Python that supports customizable port ranges, concurrency with multithreading, and basic exception handling. It’s designed for educational purposes and is capable of scanning ports on a given IP address or domain.

---

## ✨ Features

- Supports customizable port range input from the user.
- Scans ports concurrently using Python's multithreading for faster execution.
- Timeout for each port connection to avoid hanging.
- Reports open and closed ports with clear status updates.
- Displays the total time taken to complete the scan.
- Basic exception handling for invalid IP and port range inputs.

---

## ⚙️ Requirements

- Python 3.x
- A basic understanding of networking (optional)

### 🧪 Install Dependencies

1. Ensure Python 3 is installed on your machine.
2. You will need the `socket` module, which is built into Python, so no external libraries are required for this project.

---

## 🚀 Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/BLA573/port-scanner.git
   cd port-scanner

## 🧑‍💻 Example Usage

### 🛠️ Enter the required details when prompted:

- Enter the IP address or domain name to scan: 192.1.1.1 
- Enter the starting port: 50
- Enter the ending port: 500

  ---

## Output example

- Enter the IP address or domain name to scan: 192.1.1.1
- Enter the starting port: 50
- Enter the ending port: 100
- Starting scan for IP address: 192.1.1.1.
- Port 50: OPEN
- Port 51: CLOSED
- Port 52: OPEN
...

  
 - Time taken to scan: 3.45 seconds

---

## Disclaimer

This project is intended for **educational purposes only**.

By using this tool, you agree to the following:

- You are solely responsible for how you use this script.
- You will not use it to scan or probe any network, device, or system without **explicit permission**.
- The author is **not liable** for any misuse, damage, legal consequences, or ethical violations resulting from the use of this software.

Port scanning can be flagged as malicious activity. **Unauthorized use is illegal** in many countries and can result in **criminal charges**.

Use it responsibly. Use it legally.

