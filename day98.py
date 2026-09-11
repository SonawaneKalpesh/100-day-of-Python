import requests
from bs4 import BeautifulSoup

url = "https://example.com"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Get page title
    print("===== WEB SCRAPER =====")
    print("Page Title:", soup.title.string)

    # Find all headings
    print("\nHeadings:")

    headings = soup.find_all(["h1", "h2", "h3"])

    for heading in headings:
        print("-", heading.get_text(strip=True))

except requests.exceptions.RequestException as error:
    print("Request error:", error)

except Exception as error:
    print("Scraping error:", error)