import requests


def get_data(api_url):
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            return response.text
        else:
            return "Request failed with statuscode: ", str(response.status_code)
    except requests.exceptions.RequestException as s:
        return "Connection failed: ", str(s)


github_api_url = "https://api.github.com/"
github_data = get_data(github_api_url)
print("github api data:", github_data)

grthub_api_url = "https://hbhbjbjhapi.com/"
ararsebuli_data = get_data(grthub_api_url)
print("nonexistent API data: \n", ararsebuli_data)
