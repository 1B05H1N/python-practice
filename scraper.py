"""
Web Scraping Script

This script is designed to scrape the entire content from web pages using Python. It uses the requests library to 
fetch web content and displays it in a simple web server setup using Flask, making it accessible via a web browser.

This script will either fetch content from 'shinnawi.com' or from a URL passed as a query parameter.

Idea taken from https://pythongeeks.org/python-projects/#pq9
"""

import requests
from flask import Flask, request, Response, render_template_string
from bs4 import BeautifulSoup
import sys
from urllib.parse import urljoin

app = Flask(__name__)

# Check if a URL is passed via command line arguments; otherwise, use a default
if len(sys.argv) > 1:
    input_url = sys.argv[1]
else:
    input_url = 'https://shinnawi.com'

# Ensure the URL starts with http:// or https://
if not input_url.startswith(('http://', 'https://')):
    input_url = 'https://' + input_url

@app.route('/')
def scrape_site():
    # Fetch the URL from query parameters or default to 'shinnawi.com'
    url = input_url  # Use the URL specified in the command line argument
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract all text from paragraphs
            text = ' '.join(p.text for p in soup.find_all('p'))
            
            # Find all image sources
            images = [img['src'] if img['src'].startswith(('http', 'https')) else urljoin(url, img['src']) 
                      for img in soup.find_all('img') if 'src' in img.attrs]

            # Construct HTML to display results
            html_content = f"<h1>Text from {url}</h1><p>{text}</p><h2>Images:</h2>" + \
                           ''.join(f"<img src='{src}' style='max-width: 200px;'><br>" for src in images)
            
            return render_template_string(html_content)
        else:
            # Provide feedback via HTTP response on failure to retrieve the webpage
            return f"Failed to retrieve the webpage. Status code: {response.status_code}", 400
    except requests.RequestException as e:
        # Handle errors in fetching the webpage and return a server error response
        return f"Error fetching the page: {str(e)}", 500

if __name__ == "__main__":
    app.run(debug=True)