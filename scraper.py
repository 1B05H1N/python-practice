"""
Web Scraping Script

This script is designed to scrape the entire content from web pages using Python. It uses the requests library to 
fetch web content and displays it in a simple web server setup using Flask, making it accessible via a web browser.

This script will either fetch content from 'shinnawi.com' or from a URL passed as a query parameter.

Idea taken from https://pythongeeks.org/python-projects/#pq9
"""

import requests
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/')
def scrape_site():
    # Fetch the URL from query parameters or default to 'shinnawi.com'
    url = request.args.get('url', 'https://shinnawi.com')
    
    # Ensure the URL contains the HTTP/HTTPS scheme
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url  # Defaulting to 'https://' for security

    try:
        response = requests.get(url)
        if response.status_code == 200:
            # Return the raw HTML content of the site
            return Response(response.content, mimetype='text/html')
        else:
            # Provide feedback via HTTP response on failure to retrieve the webpage
            return f"Failed to retrieve the webpage. Status code: {response.status_code}", 400
    except requests.RequestException as e:
        # Handle errors in fetching the webpage and return a server error response
        return f"Error fetching the page: {str(e)}", 500

if __name__ == "__main__":
    app.run(debug=True)