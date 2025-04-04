#  Log Analyzer for Threat Detection

##  Overview
Log Analyzer is a **Flask-based web application** designed for **cybersecurity analysts** to detect suspicious activities in log files.  
It primarily analyzes **authentication logs (`auth.log`, `secure`)**, identifying **failed login attempts and brute-force attacks**.

##  Features
-  **Upload & Analyze** log files (`.log`, `.txt`, `.csv`).
-  **Detect Suspicious Activities** (failed logins, brute force attempts).
-  **Paginated Results** for better readability.
-  **Search Feature** to filter logs easily.
- ⬇**Download Processed Logs** as CSV.
- **User-Friendly Interface** using Flask & Bootstrap.

---

##  Tech Stack
| **Component** | **Technology** |
|--------------|---------------|
| **Backend**  | Python, Flask  |
| **Frontend** | HTML, Bootstrap, Jinja2 |
| **Data Processing** | Pandas, Regex |
| **File Handling** | Werkzeug |

---

##  Installation

###  Clone the Repository

git clone https://github.com/kelvinkimotho/log-analyzer.git
cd log-analyzer

###  Create & Activate Virtual Environment

python -m venv venv
source venv/bin/activate    # On macOS/Linux
venv\Scripts\activate       # On Windows

###  Install Dependencies

pip install -r requirements.txt

###  Usage
🏁 Run the Flask App
python app.py
Open http://127.0.0.1:5000/ in your browser.

### Deployed Version
https://kelvinkimotho.github.io/log_analyzer
