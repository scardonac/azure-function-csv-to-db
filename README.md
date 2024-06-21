# Azure Function - Product and Supplier Management 🚀

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](https://www.python.org/)

![GitHub watchers](https://img.shields.io/github/watchers/scardonac/azure-function-csv-to-db)
![GitHub forks](https://img.shields.io/github/forks/scardonac/azure-function-csv-to-db)


This project is an Azure Function that processes CSV files containing product and supplier information. The function updates or inserts product data into a PostgreSQL database based on the content of the CSV files. This ensures that your product and supplier information is always up-to-date and accurately reflected in your database.

## Table of Contents
- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Setup](#setup)
  - [Using Azurite](#using-azurite)
- [Usage](#usage)
  - [Running Locally](#running-locally)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)

## Introduction

Managing product and supplier data is crucial for any business that relies on accurate and timely information. This project provides a scalable and efficient solution using Azure Functions to automatically process and update product and supplier information from CSV files. 

When a new CSV file is uploaded to an Azure Blob Storage container, the function is triggered to process the file. It reads the product and supplier details, checks if the products already exist in the PostgreSQL database, and updates or inserts the records accordingly. This automation helps maintain data integrity and reduces manual efforts.

## Project Structure
```
├── README.md
├── function_app.py
├── models.py
├── local.settings.json
├── host.json
└── requirements.txt
```

### Files

- **function_app.py**: Contains the Azure Function code that processes the CSV files.
- **models.py**: Contains the SQLAlchemy models for the database tables.
- **local.settings.json**: Contains local settings for the Azure Function, including connection strings.
- **host.json**: Contains global configuration options for all functions in the app.
- **requirements.txt**: Lists the dependencies required for the project.

## Requirements

- Python 3.10 or higher 🐍
- Azure Functions Core Tools ⚙️
- PostgreSQL database 🗄️
- Azurite (for local Blob Storage emulation) 📦

## Setup

1. **Clone the repository**

    ```sh
    git clone https://github.com/scardonac/azure-function-csv-to-db.git
    cd azure-function-product-management
    ```

2. **Create and activate a virtual environment**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**

    ```sh
    pip install -r requirements.txt
    ```

4. **Configure the local settings**

    Update the `local.settings.json` file with your database connection string and Azure Blob Storage connection string:

    ```json
    {
      "IsEncrypted": false,
      "Values": {
        "FUNCTIONS_WORKER_RUNTIME": "python",
        "AzureWebJobsFeatureFlags": "EnableWorkerIndexing",
        "DATABASE_URL": "YOUR_DB_CONNECTION_STRING",
        "AzureWebJobsStorage": "YOUR_BLOB_CONNECTION_STRING",
      }
    }
    ```

### Using Azurite

Visual Studio Code uses Azurite to emulate Azure Storage services when running locally. You use Azurite to emulate the Azure Blob Storage service during local development and testing.

1. If haven't already done so, install the Azurite v3 extension for Visual Studio Code.

2. Press F1 to open the command palette, type Azurite: Start Blob Service, and press enter, which starts the Azurite Blob Storage service emulator.

3. Select the Azure icon in the Activity bar, expand Workspace > Attached Storage Accounts > Local Emulator, right-click Blob Containers, select Create Blob Container..., enter the name container1, and press Enter.
  
4. Expand Blob Containers > container1 and select Upload files....

5. Choose a file to upload to the locally emulated container. This file gets processed later by your function to verify and debug your function code. A text file might work best with the Blob trigger template code.

3. **Update `local.settings.json`**

    Modify the `local.settings.json` file to use the Azurite connection string:

    ```json
    {
      "IsEncrypted": false,
      "Values": {
        "FUNCTIONS_WORKER_RUNTIME": "python",
        "AzureWebJobsFeatureFlags": "EnableWorkerIndexing",
        "DATABASE_URL": "YOUR_DB_CONNECTION_STRING",
        "AzureWebJobsStorage": "UseDevelopmentStorage=true",
      }
    }
    ```
Verify that the local.settings.json file has "UseDevelopmentStorage=true" set for AzureWebJobsStorage, which tells Core Tools to use Azurite instead of a real storage account connection when running locally.
## Usage

### Running Locally

1. **Start the Azure Functions host**

    ```sh
    func start
    ```

2. **Trigger the function**

    Upload a CSV file to the configured Azure Blob Storage container to trigger the function. The CSV file should follow the format:

    ```csv
    SUPPLIER,PRODUCT_CODE,PRODUCT_NAME,CATEGORY,PRICE,STOCK
    Supplier A,001,Product 1,Category 1,10.99,100
    Supplier B,002,Product 2,Category 2,20.49,200
    Supplier A,003,Product 3,Category 1,15.89,150
    ```

## Acknowledgements

- [Azure Functions](https://docs.microsoft.com/en-us/azure/azure-functions/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Azurite](https://docs.microsoft.com/en-us/azure/storage/common/storage-use-azurite)
- [Azure Blob Storage](https://docs.microsoft.com/en-us/azure/storage/blobs/)

## Contact

If you have any questions or feedback, please contact [cardonasara571@gmail.com](mailto:cardonasara571@gmail.com).
