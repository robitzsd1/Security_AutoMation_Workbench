# Security_AutoMation_WorkBench
Security Automation Project Workflow
1. Project Setup
Clone Repository

Clone this repository to your local machine using:
bash
Copy code
git clone https://github.com/robitzsd1/Security_AutoMation_Workbench.git
Install Dependencies

Ensure Python is installed on your system.
Install required Python libraries:
bash
Copy code
pip install -r requirements.txt
Note: Dependencies are listed in requirements.txt.
Set Up Task Scheduler

Configure a task in Windows Task Scheduler to run scanner.py at regular intervals.
Use the guide provided in the README for step-by-step setup instructions.
Verify Environment

Ensure API key for NVD (if used) is excluded from the repository.
Test initial connectivity to confirm DNS and network configuration.
2. Workflow for Scanning and Reporting
Run Scanner

Execute the script manually for the first run:
bash
Copy code
python scanner.py
Validate output in the terminal and ensure that the report is generated in the specified directory.
Scheduled Scanning

Ensure Task Scheduler is properly configured to execute the script at your desired intervals.
Validate Output

Check the location specified for the report and ensure reports contain system information and vulnerability data.
Example location: ./reports.
3. Troubleshooting Workflow
API Connectivity Issues

Confirm API URL accessibility using:
bash
Copy code
curl -v "https://services.nvd.nist.gov/rest/json/cves/1.0"
Resolve network or DNS issues as per project documentation.
Task Scheduler Errors

Verify paths and permissions in the Task Scheduler configuration.
Ensure the Python executable and script paths are accurate.
Report Validation

Manually verify report data for accuracy.
Debug issues with missing or incorrect data.
4. Maintenance Workflow
Update Dependencies

Regularly update Python libraries:
bash
Copy code
pip install --upgrade -r requirements.txt
Monitor Task Scheduler

Periodically check Task Scheduler to ensure the scheduled task is running as expected.
Update schedule timing based on project requirements.
Expand Script Functionality

Integrate new features (e.g., alternative APIs, visualization tools).
Maintain consistent code documentation for any updates.
5. Future Enhancements
Add support for additional operating systems (e.g., macOS, Linux).
Incorporate alternative APIs for diversified data sources.
Implement visual dashboards for reporting.
