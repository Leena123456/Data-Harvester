import os
import time
from requests_html import HTMLSession

# Clear the screen
os.system('cls' if os.name == 'nt' else 'clear')

# Get user input
Query = input('Enter Your Query : ')
Limit = int(input('Enter No. Of Urls To Scrape : '))

# Open a file to write the results
file = open('Results.txt', 'w')

# Create an HTML session
s = HTMLSession()

# Define headers to mimic a real browser request
headers = {
    'authority': 'www.google.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.5',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62',
}

# Define search parameters
params = {
    'q': Query,
    'num': Limit,
}

# Send a GET request to Google Search
response = s.get('https://www.google.com/search', headers=headers, params=params)

# Print the response text for debugging
#print(response.text)

# Check for different response conditions
if 'did not match any documents' in response.text:
    exit('No Results Found')
elif 'Our systems have detected unusual traffic from your computer' in response.text:
    exit('Captcha Triggered!\nUse VPN Or Try After Sometime.')
else:
    # Extract and print URLs from the search results
    links = list(response.html.absolute_links)
    count = 0
    for url in links:
        if 'google' not in url:
            print(url)
            file.write(url + '\n')
            count += 1
            if count >= Limit:
                break
            # Add a delay between requests to avoid being blocked
            time.sleep(2)

# Close the file
file.close()
