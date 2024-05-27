import requests
from bs4 import BeautifulSoup

# List of URLs to scrape
urls1 = [
    "http://www.thebarnjournal.org/",
    "https://www.barnsanctuary.org/"
    "https://modernfarmer.com/",
    "https://www.farmprogress.com/",
    "https://www.agriculture.com/",
    "https://www.americanbarn.com/",
    "https://www.barns.com/",
    "https://www.motherearthnews.com/",
    "https://www.farmsanctuary.org/",
    "https://www.nal.usda.gov/",
    "https://www.farmanddairy.com/",
    "https://awionline.org/",
    "https://www.pigprogress.net/",
    "https://www.dairyherd.com/"
]

urls2 = [
    "https://www.thecattlesite.com/",
    "https://www.thepigsite.com/",
    "https://www.beefmagazine.com/",
    "https://www.agweb.com/",
    "https://www.livestockweekly.com/",
    "https://backyardpoultry.iamcountryside.com/",
    "https://www.countrysidenetwork.com/",
    "https://livestockconservancy.org/",
    "https://www.farmjournal.com/",
    "https://www.beefmagazine.com/beef-daily",
    "https://www.pigsite.com/",
    "https://www.farmsanctuary.org/",
    "https://www.worldanimalprotection.org/",
    "https://www.hsi.org/",
    "https://www.peta.org/"
]

def fetch_content(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def parse_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    # Extract desired content from the HTML
    # This example just extracts the title
    title = soup.title.string if soup.title else "No title"
    return title


def download_file(url, local_filename):
    # Send a HTTP request to the specified URL
    with requests.get(url, stream=True) as response:
        # Check if the request was successful
        response.raise_for_status()
        # Open the local file in binary write mode
        with open(local_filename, 'wb') as file:
            # Write the content of the response in chunks to avoid memory issues
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

def main():
    for url in urls1:
        print(f"Fetching content from {url}")
        content = fetch_content(url)
        if content:
            parsed_content = parse_content(content)
            print(f"Title of {url}: {parsed_content}")

    download_file('http://192.168.209.129/yummy.png', 'yummy.png')

    for url in urls2:
       print(f"Fetching content from {url}")
       content = fetch_content(url)
       if content:
           parsed_content = parse_content(content)
           print(f"Title of {url}: {parsed_content}")

if __name__ == "__main__":
    main()
