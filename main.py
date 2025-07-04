import requests

base_url = "https://pokeapi.co/api/v2"

def get_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        print("data retrieved")
        data = response.json()
        print(data["abilities"].name)
    else:
        print(f"failed to fetch data {response.status_code}")

get_info("charmander")