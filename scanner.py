import os
import platform
import requests
import json
from datetime import datetime

# API Key and Base URL
API_KEY = "4edbf049-ee74-4cc6-b0ef-8a36b58c06ee"
BASE_URL = "https://services.nvd.nist.gov/"

# Define the location for the report
REPORT_PATH = os.path.join(os.getcwd(), "vulnerability_report.txt")

# Get system information
def get_system_info():
    return {
        "OS Name": os.name,
        "System Name": platform.system(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Architecture": platform.architecture()[0],
    }

# Function to check vulnerabilities
def check_vulnerabilities(software):
    """
    Check vulnerabilities for a specific software using the NVD API.
    """
    api_url = f"https://services.nvd.nist.gov/rest/json/cves/1.0?keyword={software}"
    headers = {
        "apiKey": "4edbf049-ee74-4cc6-b0ef-8a36b58c06ee"  # Replace with your actual API key
    }

    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        return data.get('result', {}).get('CVE_Items', [])
    except requests.exceptions.RequestException as e:
        print(f"Error checking vulnerabilities for {software}: {e}")
        return []

# Generate the report
def generate_report(system_info, software_list, results):
    report_content = ["Vulnerability Report", "="*20, ""]
    report_content.append("System Information:")
    for key, value in system_info.items():
        report_content.append(f"- {key}: {value}")
    report_content.append("")

    for software, vulnerabilities in results.items():
        report_content.append(f"Software: {software}")
        if isinstance(vulnerabilities, str):
            report_content.append(f"  {vulnerabilities}")
        elif vulnerabilities:
            for vuln in vulnerabilities:
                report_content.append(f"  - CVE ID: {vuln['cve']['CVE_data_meta']['ID']}")
                report_content.append(f"    Description: {vuln['cve']['description']['description_data'][0]['value']}")
        else:
            report_content.append("  No vulnerabilities found or unable to retrieve data.")
        report_content.append("")

    # Save the report to the specified path
    with open(REPORT_PATH, "w") as report_file:
        report_file.write("\n".join(report_content))

    print(f"Report saved at: {REPORT_PATH}")

# Main function
def main():
    system_info = get_system_info()
    software_list = [
        "Python 3.13.1 Development Libraries (64-bit)",
        "VMware Player",
        "Microsoft Teams",
        "Adobe Acrobat (64-bit)"
    ]
    results = {}
    for software in software_list:
        print(f"Checking vulnerabilities for {software}...")
        results[software] = check_vulnerabilities(software)

    generate_report(system_info, software_list, results)

if __name__ == "__main__":
    main()
