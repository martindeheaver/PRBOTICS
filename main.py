
install requests

# Your NewsCatcher API key
api_key = "VhDOFO0GZ0i_ZSHQvTllozj-BxWVnUcr"

# Setting up the request parameters
params = {
    "q": "artificial intelligence",  # Your search query
    "lang": "en",  # Language code (optional)
    "sort_by": "date",  # Sort by date
    "page": 1,  # Page number (optional)
    "page_size": 10  # Number of results per page (optional, max: 100)
}

# Making the GET request to the NewsCatcher API
response = requests.get(
    "https://api.newscatcherapi.com/v2/search",
    headers={"x-api-key": api_key},
    params=params
)

# Checking if the request was successful
if response.status_code == 200:
    data = response.json()
    # Printing out the title and link of each article
    for article in data["articles"]:
        print(f"Title: {article['title']}\nLink: {article['link']}\n")
else:
    print(f"Failed to fetch articles. Status code: {response.status_code}")
