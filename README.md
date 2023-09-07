# Phones data scraper

Scrapy spider that scrapes phones data from website: https://www.productindetail.com/

## Libraries

Before getting started, ensure you have the following libraries installed on your system:

1. **Scrapy.** Web scraping framework. Install it using:`pip install scrapy`

2. **PyMongo.** Python driver for MongoDB. Install it using: `pip install pymongo`

## MongoDB Installation Guide

**Step 1: Visit the MongoDB Download Page**

Begin by visiting the MongoDB download page, which can be found at [MongoDB Download Page](https://www.mongodb.com/try/download/community).

**Step 2: Choose Your MongoDB Version**

Select the version of MongoDB Community Edition that matches your operating system. Click on the download link to initiate the process.

**Step 3: Run the Installer**

After downloading the installer, locate the downloaded file and run it. The installation wizard will guide you through the setup process.

**Step 4: Follow Installation Instructions**

Follow the on-screen installation instructions that are specific to your platform. MongoDB provides detailed guidance to ensure a installation.

**Step 5: Creating database**

Create in MongoDB database named `phone_data` and collection name `phones`

## Providing database information 

Since the database information is not critical and this project is open, there is no need to store the database login information in environment variables. Database login information can be passed in `settings.py`

```python
MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "phone_data"
MONGODB_COLLECTION = "phones"
```

## Running the scraper

To run the Scrapy spider and start the scraping process, follow these steps:

**Step 1: Navigate to the spider's directory:**
`cd phonesScraper/phonesScraper`

**Step 2: Run the spider using the following command:**
`scrapy crawl phones`
