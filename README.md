# Personal Cyber Tool (PCT) 🛡️

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](#contributing)

**Personal Cyber Tool (PCT)** is an advanced, modular Python-based Open-Source Intelligence (OSINT) framework. Designed for security researchers, penetration testers, and digital investigators, PCT streamlines information gathering, footprinting, and digital reconnaissance by aggregating multiple OSINT search vectors into a single, cohesive command-line interface.

---

## 🚀 Key Features

- **Modular Architecture:** Easily enable, disable, or extend specific OSINT modules.
- **Multi-Vector Reconnaissance:** Perform automated lookups across diverse digital footprints.
    - **Email Intelligence:** Check breach databases, associated social accounts, and domain registrations.
    - **Username Enumeration:** Scan popular platforms, forums, and developer repositories for username footprints.
    - **Domain & IP Recon:** Gather WHOIS records, DNS enumeration, subdomain discovery, and geolocation data.
    - **Phone Number Analysis:** Extract carrier data, line type, and international formatting details.
- **Asynchronous Execution:** Built with performance in mind, utilizing asynchronous requests to minimize scanning time.
- **Structured Reporting:** Export findings seamlessly into JSON, CSV, or human-readable formats for documentation and analysis.

---

## 📂 Project Structure

```text
Personal-Cyber-Tool/
│
├── core/                  # Core framework logic and configuration handlers
├── modules/               # Individual OSINT scanning vectors
│   ├── email_scanner.py
│   ├── username_scanner.py
│   ├── domain_scanner.py
│   └── phone_scanner.py
│
├── outputs/               # Generated reports and scan logs
├── requirements.txt       # Project dependencies
├── main.py                # Main CLI entry point
└── README.md              # Project documentation
```

---

## ⚙️ Installation & Setup

Ensure you have **Python 3.8 or higher** installed on your system. Follow these steps to set up the environment locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/Personal-Cyber-Tool.git
   cd Personal-Cyber-Tool
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 💻 Usage

PCT provides an interactive CLI interface as well as direct command flags for rapid assessment.

To launch the interactive main menu:
```bash
python main.py
```

To run a specific module directly (e.g., username search):
```bash
python main.py --username target_user
```

To output results to a specific file format:
```bash
python main.py --domain example.com --output json --output-file results.json
```

---

## 🛠️ Configuration

Some OSINT modules require API keys (e.g., Shodan, HaveIBeenPwned, Hunter.io) to function at full capacity. 
1. Copy the template configuration file:
   ```bash
   cp config.example.json config.json
   ```
2. Insert your respective API keys into `config.json`. The framework will automatically detect and load them.

---

## ⚠️ Disclaimer

This tool is created for **educational purposes, authorized security testing, and defensive research only**. The authors and maintainers assume **no liability** and are not responsible for any misuse or damage caused by this program. Users must ensure they have explicit, written permission from target owners before conducting any reconnaissance activities.

---

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git origin push feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.
