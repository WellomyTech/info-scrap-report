import requests
API_Key = "AIzaSyAyM4cH4iPmNxWBC0TD7bWrYLSJQcr31Eo"
SEARCH_ENGINE_ID = "d21cabf68fbd94ab7"
query = "Juan Dalmau Puerto Rico"

base_url = "https://cse.google.com/cse?cx=d21cabf68fbd94ab7"

params = {
    "key": API_Key,
    "cx": SEARCH_ENGINE_ID,
    "q": query,
    "num": 10
}

response = requests.get(base_url, params=params)

# Process the response
try: 

    if response.status_code == 200:
        data = response.json()
        # Extracting search results
        if "items" in data:
            for item in data["items"]:
                print(f"Title: {item['title']}")
                print(f"Link: {item['link']}")
                print(f"Snippet: {item['snippet']}\n")
        else:
            print("No search results found.")
except Exception as e:
    print(e)       
    print(f"Error: {response.status_code}")
    print(response)