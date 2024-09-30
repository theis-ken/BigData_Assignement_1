# Scrapy Project - Book Scraper

## Overview
This project is a **Scrapy spider** designed to scrape book information from the website [Books to Scrape](https://books.toscrape.com/). The spider extracts the following data for each book:

- **Book Titles**
- **Prices**
- **Availability Status**

The scraped data is stored in a **MongoDB** database for further analysis and visualization.

## Spider Functionality

### How the Spider Works
1. **Spider Initialization:**
   The spider begins by sending an HTTP request to the main page of the [Books to Scrape](https://books.toscrape.com/) website.

2. **Parsing Pages:**
   The spider crawls through multiple pages, extracting data for each book listed on the website. It does this by locating the specific HTML elements that contain the following information:
   - **Title**: Extracted from the `<h3>` tag containing the title of the book.
   - **Price**: Extracted from the price tag (`<p class="price_color">`).
   - **Availability**: Extracted from the availability status (`<p class="instock availability">`).

3. **Handling Pagination:**
   The spider automatically follows the pagination links at the bottom of each page to ensure that it scrapes data from all pages of the website. It does this by identifying the "Next" button and recursively calling the `parse` method to navigate to the next page.

4. **Data Cleaning and Normalization:**
   The spider performs basic data cleaning, such as:
   - **Stripping extra spaces** from text fields.
   - **Converting prices** from strings to float values for further processing.
   - **Handling availability** by ensuring consistency in how "In stock" or "Out of stock" statuses are represented.

5. **Storing Data:**
   After the data is extracted and cleaned, it is stored in a MongoDB database. Each book's data is saved as a document in the `books` collection of the `books_db` database.

6. **Error Handling:**
   The spider is equipped with basic error handling to manage failed requests and retries. If the spider encounters an issue while scraping a particular page, it logs the error and moves on to the next page without interrupting the overall process.

### Data Fields
Here are the specific data fields the spider extracts and stores in MongoDB:
- **Title**: The name of the book.
- **Price**: The price of the book (converted to a float).
- **Availability**: Whether the book is available or not (e.g., "In stock" or "Out of stock").

### Logging
The spider uses logging to record its activity. You can check the logs to track the spider's progress and identify any issues encountered during the scraping process.

## Requirements
Before running the project, ensure you have the following installed:

- **Python** 3.6 or higher
- **MongoDB**
- **Scrapy**
- **pymongo** (for MongoDB integration)

## Installation Steps

1. **Clone the Repository**  
   Open your terminal and run:
   ```bash
   git clone https://github.com/theis-ken/BigData_Assignement_1
   cd Scrappy
   ```

2. **Required Packages**
   Ensure pymongo is installed. You can install it using:
   ```bash
   pip install pymongo
   ```

## Running the Spider
   To start the spider and begin scraping data, navigate to the Scrappy\BigData\BigData\spiders\ directory and use the following command:
   ```bash
   scrapy crawl books
```

## Data Storage

The scraped data will be stored in the books collection of the books_db database in MongoDB.

## Visualizing the Data

After scraping, you can visualize the data by running the visualize_data.py script. This script includes two basic diagrams:

- A histogram of book prices
- A pie chart showing the availability of books

Thank you for reading =)
