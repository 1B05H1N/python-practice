import requests
from bs4 import BeautifulSoup
import sys

def scrape_quotes(url):
    # Ensure the URL contains the HTTP/HTTPS scheme
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url  # You can also choose to default to 'https://'

    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.find_all('span', class_='text')
        for quote in quotes:
            print(quote.text)
    else:
        print("Failed to retrieve the webpage")
        print("Status code:", response.status_code)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        scrape_quotes(url)
    else:
        print("Please provide a URL as a command-line argument.")
