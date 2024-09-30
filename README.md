# Scrapy Project - Book Scraper

## Overview
This project is a **Scrapy spider** designed to scrape book information from the website [Books to Scrape](https://books.toscrape.com/). The spider extracts the following data:

- **Book Titles**
- **Prices**
- **Availability Status**

The scraped data is stored in a **MongoDB** database.

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
   git clone https://github.com/theis-ken/BigData_Ex1
   cd Scrappy

2. **Required Packages**
   Have pymongo installed. You can install it using:
   ```bash
   pip install pymongo

## Running the Spider
   To start the spider and begin scraping data, navigate to the Scrappy\BigData\BigData\spiders\ directory and use the following command:
   ```bash
   scrapy crawl books



## Data Storage

The scraped data will be stored in the books collection of the books_db database in MongoDB.

## Visualizing the Data

After scraping, you can visualize the data by running the visualize_data.py script. This script includes two basic diagrams:

- A histogram of book prices
- A pie chart showing the availability of books
