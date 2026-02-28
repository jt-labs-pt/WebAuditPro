# 🌐 Domain & Web Intelligence Tool

A Python-based utility designed for automated domain reconnaissance and web data extraction. This tool integrates WHOIS lookups with advanced web scraping to provide a comprehensive overview of target websites.

---

## ✨ Features

* **WHOIS Insight:** Retrieves domain registration dates, registrar info, and expiration status.
* **Smart Scraping:** Extracts structured data and links using `BeautifulSoup4`.
* **Automated Export:** Organizes gathered intelligence into JSON and ZIP archives.
* **One-Click Setup:** Includes a dedicated Windows bootstrapper to handle environment configuration.

---

## 🚀 Quick Start (Windows)

If you are on Windows, you don't need to manually configure Python or install libraries. 

1.  **Download** the repository as a ZIP (or clone it).
2.  Extract the files to a local folder.
3.  Run **`start_me.bat`**.
    * *The script will automatically detect Python, install it if missing, create a virtual environment, and install all dependencies.*
4.  The application will launch immediately after the setup.

---

## 🛠 Manual Installation (Developers)

If you prefer to set up the environment manually or are using **Linux/macOS**:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/jt-labs-pt/WebAuditPro.git](https://github.com/jt-labs-pt/WebAuditPro.git)
    cd WebAuditPro
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # Windows:
    venv\Scripts\activate
    # Linux/macOS:
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install python-whois requests beautifulsoup4
    ```

4.  **Run the app:**
    ```bash
    python webaudit.py
    ```

---

## 📦 Dependencies

This project relies on the following open-source libraries:
* [python-whois](https://pypi.org/project/python-whois/) - Domain WHOIS retrieval.
* [Requests](https://pypi.org/project/requests/) - HTTP library for Python.
* [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) - HTML/XML parsing.

---

## 🇵🇹 About the Author
Developed by an independent creator in **Portugal**.  
Feel free to open an **Issue** or a **Pull Request** if you'd like to contribute!

---

