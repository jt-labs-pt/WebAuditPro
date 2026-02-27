import whois
import requests
from bs4 import BeautifulSoup
import json
import zipfile
import os
from urllib.parse import urljoin, urlparse
from datetime import datetime

class WebAuditPro:
    def __init__(self, url):
        self.url = url if url.startswith('http') else f'https://{url}'
        self.domain = urlparse(self.url).netloc
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.folder_name = f"audit_{self.domain}_{self.timestamp}"
        self.assets_folder = os.path.join(self.folder_name, "assets")
        self.report = {}

    def setup_folders(self):
        if not os.path.exists(self.assets_folder):
            os.makedirs(self.assets_folder)

    def download_asset(self, asset_url, subfolder):
        """Downloads CSS or JS files for analysis."""
        try:
            name = os.path.basename(urlparse(asset_url).path)
            if not name: return None
            
            path = os.path.join(self.assets_folder, subfolder, name)
            os.makedirs(os.path.dirname(path), exist_ok=True)
            
            response = requests.get(asset_url, timeout=5)
            with open(path, "w", encoding='utf-8') as f:
                f.write(response.text)
            return path
        except:
            return None

    def get_whois_data(self):
        print(f"[*] Fetching WHOIS data for {self.domain}...")
        try:
            w = whois.whois(self.domain)
            self.report['whois_info'] = {
                "registrar": w.registrar,
                "creation_date": str(w.creation_date),
                "expiration_date": str(w.expiration_date),
                "name_servers": w.name_servers
            }
        except:
            self.report['whois_info'] = {"error": "WHOIS lookup failed"}

    def full_audit(self):
        print(f"[*] Starting Full Audit on {self.url}...")
        self.setup_folders()
        
        try:
            response = requests.get(self.url, timeout=15)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # 1. Analyze Security Headers
            self.report['headers'] = dict(response.headers)
            
            # 2. Extract and Download CSS & JS
            css_files = []
            for css in soup.find_all("link", rel="stylesheet"):
                href = urljoin(self.url, css.get("href"))
                path = self.download_asset(href, "css")
                if path: css_files.append(href)

            js_files = []
            for js in soup.find_all("script", src=True):
                src = urljoin(self.url, js.get("src"))
                path = self.download_asset(src, "js")
                if path: js_files.append(src)

            self.report['assets_found'] = {
                "css_count": len(css_files),
                "js_count": len(js_files),
                "css_urls": css_files,
                "js_urls": js_files
            }

            # 3. Save Main HTML
            with open(os.path.join(self.folder_name, "index.html"), "w", encoding='utf-8') as f:
                f.write(response.text)

            return True
        except Exception as e:
            print(f"[!] Error: {e}")
            return False

    def create_zip(self):
        """Zips everything for the final sale package."""
        with open(os.path.join(self.folder_name, "security_report.json"), "w") as f:
            json.dump(self.report, f, indent=4)

        zip_name = f"{self.folder_name}.zip"
        with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(self.folder_name):
                for file in files:
                    full_path = os.path.join(root, file)
                    arcname = os.path.relpath(full_path, self.folder_name)
                    zipf.write(full_path, arcname)
        
        print(f"\n[DONE] Package ready: {zip_name}")

if __name__ == "__main__":
    target = input("Target Domain (e.g. google.com): ")
    audit = WebAuditPro(target)
    if audit.full_audit():
        audit.get_whois_data()
        audit.create_zip()