"""
Website Checker Application
Taken from https://pythongeeks.org/python-website-connectivity-checker-project/

This script is a simple website checker application built using Tkinter.
It allows the user to enter a website URL and checks if the website is up or down.
If the website is up, it opens the URL in the default web browser.
"""

import urllib.request
from tkinter import Tk, Label, Entry, Button
import webbrowser  # Standard library for opening web pages in a browser

# Setup the main window
window = Tk()
window.title("Website Checker")
window.geometry("400x200")

# Create a label to describe what the application does
header = Label(window, text="Enter a website to check if it is up or down.")
header.pack(padx=10, pady=10)

# Entry widget for inputting the website URL
entry = Entry(window)
entry.pack(padx=10, pady=10, ipadx=100, ipady=5)

# Label to display the result
result = Label(window)
result.pack(padx=10, pady=10)

def check_website():
    url = entry.get().strip()
    # Ensure URL starts with http:// or https://, otherwise prepend http://
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    
    try:
        # Attempt to open the website URL with a timeout
        response = urllib.request.urlopen(url, timeout=10)
        response.close()  # Close the response
        result.config(text="Website is up")
        webbrowser.open(url)  # Open URL in the default web browser
    except urllib.request.URLError as e:
        if hasattr(e, 'reason'):
            result.config(text=f"Website is down. Reason: {e.reason}")
        elif hasattr(e, 'code'):
            result.config(text=f"Website is down. HTTP error code: {e.code}")
    except Exception as e:
        # Generic exception to catch unexpected errors
        result.config(text=f"An error occurred: {str(e)}")

# Button to trigger the check_website function
button = Button(window, text="Check Website", command=check_website)
button.pack(padx=10, pady=10, ipadx=10, ipady=5)

# Start the Tkinter event loop
window.mainloop()