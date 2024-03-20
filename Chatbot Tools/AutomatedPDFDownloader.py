import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def download_pdf(url, save_dir):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
        'Referer': 'https://citizenslanka.org/'
    }
    response = requests.get(url, headers=headers)
    filename = os.path.join(save_dir, url.split("/")[-1])
    with open(filename, 'wb') as f:
        f.write(response.content)

def main():
    url = "https://citizenslanka.org/laws-of-sri-lanka/" # Website directory
    save_dir = "/Users/omar/Projects/PycharmProjects/Webscrape/LawData"  # directory to save PDFs

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    print("Scraping URL:", url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    pdf_count = 0
    for link in soup.find_all('a', href=True):
        href = link['href']
        if href.endswith('.pdf'):
            pdf_count += 1
            pdf_url = urljoin(url, href)
            download_pdf(pdf_url, save_dir)
            print(f"Downloaded: {pdf_url}")

    print("Total PDFs downloaded:", pdf_count)

if __name__ == "__main__":
    main()
