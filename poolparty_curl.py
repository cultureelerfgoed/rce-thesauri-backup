import requests
import json
from getpass import getpass

# Define the API credentials
api_username = input("Enter your PoolParty username: ")
api_password = getpass("Enter your PoolParty password: ")  # This will securely hide the password input

# Define the PoolParty project number
poolparty_project_number = "3deabaf3-f49f-4eapc0-9490-03ed89ef8550"

# Define the API URL using the project number
api_url = f"https://digitaalerfgoed.poolparty.biz/PoolParty/api/projects/{poolparty_project_number}/export"

# Define the JSON payload
json_payload = {
    "prettyPrint": True,
    "format": "TriG",
    "modules": ["concepts"]
}

# Set the output file path on your desktop
output_file = f"C:\\Users\\Ruben\\Documents\\05. RCE\\rn-test.trig"

# Perform the API request using the requests library
headers = {"Content-Type": "application/json"}
auth = (api_username, api_password)
response = requests.post(api_url, headers=headers, data=json.dumps(json_payload), auth=auth)

# Check if the request was successful
if response.status_code == 200:
    with open(output_file, "wb") as file:
        file.write(response.content)
else:
    print(f"API request failed with status code {response.status_code}")
