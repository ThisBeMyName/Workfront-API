import requests  # For making HTTP requests
import argparse  # For parsing command-line arguments

# Set up command-line arguments: project ID and new status
parser = argparse.ArgumentParser(description="Update Workfront project status")
parser.add_argument("project_id", help="The ID of the Workfront project to update")
parser.add_argument("status", help="The new status code (e.g., CUR, CPL, ONH)")
args = parser.parse_args()

# Your API key and Workfront domain (replace with real values)
API_KEY = 'YOUR-API-KEY'
DOMAIN = 'https://YOUR-DOMAIN.workfront.com'

# API endpoint URL for the specific project
url = f"{DOMAIN}/attask/api/v19.0/proj/{args.project_id}"

# Headers and query params for the request
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
params = {'apiKey': API_KEY}

# Data payload with new status
payload = {'status': args.status}

# Send PUT request to update the project status
response = requests.put(url, headers=headers, params=params, data=payload)

# Print success or failure message based on response
if response.status_code == 200:
    print(f"✅ Project {args.project_id} updated to status '{args.status}' successfully!")
else:
    print("❌ Failed to update project status.")
    print("Status Code:", response.status_code)
    print("Response:", response.text)
