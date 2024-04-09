import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def download_pdf(url, save_dir):
    """
    Download a PDF file from the given URL and save it to the specified directory.

    Args:
    - url (str): The URL of the PDF file to download.
    - save_dir (str): The directory to save the downloaded PDF file.
    """
    # Define custom headers to mimic a web browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
        'Referer': 'https://citizenslanka.org/'
    }
    
    # Send a GET request to download the PDF file
    response = requests.get(url, headers=headers)
    
    # Extract the filename from the URL
    filename = os.path.join(save_dir, url.split("/")[-1])
    
    # Save the PDF file to the specified directory
    with open(filename, 'wb') as f:
        f.write(response.content)

def main():
    """
    Main function to scrape the website and download PDF files.
    """
    # Define the URL of the website directory and the directory to save PDFs
    url = "https://citizenslanka.org/laws-of-sri-lanka/"
    save_dir = "/Users/omar/Projects/PycharmProjects/Webscrape/LawData"

    # Create the save directory if it does not exist
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    print("Scraping URL:", url)
    
    # Define custom headers to mimic a web browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
    }
    
    # Send a GET request to the website
    response = requests.get(url, headers=headers)
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Initialize a counter for the number of downloaded PDFs
    pdf_count = 0
    
    # Iterate through all <a> tags in the HTML content
    for link in soup.find_all('a', href=True):
        href = link['href']
        
        # Check if the link ends with '.pdf' to identify PDF files
        if href.endswith('.pdf'):
            pdf_count += 1
            pdf_url = urljoin(url, href)
            
            # Download the PDF file
            download_pdf(pdf_url, save_dir)
            
            print(f"Downloaded: {pdf_url}")

    print("Total PDFs downloaded:", pdf_count)

if __name__ == "__main__":
    main()
