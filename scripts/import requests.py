import requests
from requests.auth import HTTPBasicAuth

# Replace these with your actual URL and credentials
url = "https://digitaalerfgoed-test.poolparty.biz/PoolParty/api/thesaurus/3deabaf3-f49f-4ec0-9490-03ed89ef8550/concept?properties=skos:hiddenLabel,skos:broader,https://data.cultureelerfgoed.nl/term/id/rn/aad68581-3960-4faf-9758-8ff6d65810d3&concept=https://data.cultureelerfgoed.nl/term/id/rn/62e59073-a069-42df-9eba-5e2699643345"
username = "apiuser_testschalk"
password = "Trein#130"

# Make a GET request with authentication
response = requests.get(url, auth=HTTPBasicAuth(username, password))

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print("Request successful!")
    print("Response:")
    print(response.text)
else:
    print(f"Request failed with status code {response.status_code}")
    print("Response:")
    print(response.text)
