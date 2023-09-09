# `BingImageScraper` Class Documentation

## Overview

The `BingImageScraper` class is a Python class designed to search for images on Bing Image Search and download them to your local machine. It offers flexibility in specifying search terms, the number of images to download, and the maximum number of result pages to scrape. Additionally, it automatically organizes the downloaded images into folders and creates a zip file for easy storage and sharing.

## Constructor

### `__init__(self, search_term, num_images=100, max_pages=10)`

- `search_term` (str): The search term or phrase used to query Bing Image Search.
- `num_images` (int): The number of images to download (default is 100).
- `max_pages` (int): The maximum number of search result pages to scrape (default is 10).

## Methods

### `search_and_download_images(self)`

This method initiates the search and download process based on the provided search term and settings.

#### Parameters

None.

#### Usage Example

```python
scraper = BingImageScraper("Coronary angiography", num_images=50, max_pages=5)
scraper.search_and_download_images()
```

## Attributes

- `search_term` (str): The search term used for image search.
- `num_images` (int): The number of images to download.
- `max_pages` (int): The maximum number of search result pages to scrape.

## Usage Example

```python
# Create a BingImageScraper instance
scraper = BingImageScraper("Coronary angiography", num_images=50, max_pages=5)

# Initiate the image search and download process
scraper.search_and_download_images()
```

## Error Handling

The class includes basic error handling to handle exceptions that may occur during the search and download process. If an error occurs while processing an image, it will be logged, allowing the script to continue searching and downloading the remaining images.

## License

This class and the associated script are licensed under the MIT License. You can find more details in the [LICENSE](https://github.com/dheiver/BingImageScraper/blob/main/LICENSE) file.

## Dependencies

This class relies on the following Python libraries:

- `requests`: Used for making HTTP requests to Bing Image Search.
- `beautifulsoup4`: Used for parsing HTML content from the search results page.

You can install these libraries using `pip` as mentioned in the prerequisites section of the [README](https://github.com/dheiver/BingImageScraper#prerequisites).

## Contributing

Contributions to this class and the associated project are welcome. Please follow the guidelines in the [CONTRIBUTING](https://github.com/dheiver/BingImageScraper/blob/main/CONTRIBUTING.md) file to contribute.

## Acknowledgments

This class was developed by [Your Name] as part of [Project Name]. We acknowledge and appreciate the contributions of the open-source community in developing and maintaining the libraries used by this class.

## Contact

For questions, suggestions, or issues related to this class, please feel free to [contact us](mailto:your.email@example.com).

---

This Markdown documentation provides an overview of the `BingImageScraper` class, its constructor, methods, attributes, error handling, licensing, dependencies, contributing guidelines, acknowledgments, and contact information. You can use this documentation as part of your project's README or documentation files.
