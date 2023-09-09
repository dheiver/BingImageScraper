import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote
import json
import zipfile

class BingImageScraper:
    def __init__(self, search_term, num_images=100, max_pages=10):
        self.search_term = search_term
        self.num_images = num_images
        self.max_pages = max_pages

    def search_and_download_images(self):
        # Directory where you want to save the images
        save_directory = "imagens"
        os.makedirs(save_directory, exist_ok=True)

        # List to store downloaded image file names
        downloaded_images = []

        # Loop to navigate through multiple result pages
        for page in range(self.max_pages):
            # URL for Bing Image search with pagination
            start = page * 50  # 50 results per page
            url = f"https://www.bing.com/images/search?q={self.search_term}+size:large&first={start}"

            # User agent headers to mimic a browser
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

            # Make an HTTPS request with SSL certificate verification
            img_response = requests.get(url, headers=headers)

            # Check if the request was successful
            if img_response.status_code == 200:
                # Parse the page content using BeautifulSoup
                soup = BeautifulSoup(img_response.text, 'html.parser')

                # Find all <a> tags containing links to the images
                image_links = soup.find_all('a', class_='iusc')

                # Iterate over the image links
                for link in image_links:
                    try:
                        # Get the JSON image data
                        data = unquote(link.get('m'))

                        # Parse the JSON
                        image_data = json.loads(data)

                        # Get the image URL
                        img_url = image_data['murl']

                        # Check if the URL ends with .png or .jpg (desired formats)
                        if img_url.endswith(('.png', '.jpg')) and len(downloaded_images) < self.num_images:
                            # Get the file name from the image URL
                            img_filename = os.path.join(save_directory, os.path.basename(img_url))

                            # Download the image
                            img_response = requests.get(img_url)

                            # Check if the download was successful
                            if img_response.status_code == 200:
                                with open(img_filename, 'wb') as img_file:
                                    img_file.write(img_response.content)

                                # Rename the image with a new name
                                new_img_filename = os.path.join(save_directory, f"image_{len(downloaded_images) + 1}.jpg")
                                os.rename(img_filename, new_img_filename)
                                print(f"Image downloaded and renamed: {new_img_filename}")
                                downloaded_images.append(new_img_filename)
                            else:
                                print(f"Failed to download the image: {img_url}")
                    except Exception as e:
                        print(f"Error processing image: {str(e)}")

        # Compress the images into a zip file
        if downloaded_images:
            zip_filename = "imagens.zip"
            with zipfile.ZipFile(zip_filename, 'w') as zipf:
                for img in downloaded_images:
                    zipf.write(img, os.path.basename(img))

            print(f"All images have been compressed into {zip_filename}")
        else:
            print("No images were found.")

# Example of using the class
if __name__ == "__main__":
    search_terms = [
        "Coronary angiography procedure",
        "Cardiac catheterization angiogram",
        "Heart vessel examination",
        "Coronary artery X-ray"
    ]
    num_images = 100  # Number of images per search term
    max_pages = 10    # Maximum number of pages to navigate per term

    for term in search_terms:
        scraper = BingImageScraper(term, num_images, max_pages)
        scraper.search_and_download_images()
