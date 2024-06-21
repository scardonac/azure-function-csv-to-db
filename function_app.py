import azure.functions as func
import csv
import codecs
import os
import logging
from typing import Generator, Dict
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session as SessionType
from models import Product, Supplier
from datetime import datetime

app = func.FunctionApp()

def get_database_session() -> SessionType:
    """
    Establishes a connection to the database and returns a session object.

    Returns:
        SessionType: SQLAlchemy session object.
    """
    DATABASE_URL = os.getenv("DATABASE_URL")
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    return Session()

def process_csv(file_content: Generator[str, None, None], session: SessionType) -> None:
    """
    Processes a CSV file and updates the database with product and supplier information.

    Args:
        file_content (Generator[str, None, None]): Decoded content of the CSV file.
        session (SessionType): SQLAlchemy session object.
    """
    reader = csv.DictReader(file_content)
    for line in reader:
        supplier_name = line.get('SUPPLIER')
        product_code = line.get('PRODUCT_CODE')
        product_name = line.get('PRODUCT_NAME')
        category = line.get('CATEGORY')
        price = line.get('PRICE')
        stock = line.get('STOCK')

        supplier = session.query(Supplier).filter_by(name=supplier_name).first()
        if not supplier:
            supplier = Supplier(name=supplier_name)
            session.add(supplier)
            session.commit()
            logging.info("Supplier created: %s", supplier_name)

        product = session.query(Product).filter_by(code=product_code).first()
        if product:
            if (product.name != product_name or
                product.category != category or
                product.price != price or
                product.stock != stock or
                product.supplier_id != supplier.id):

                product.name = product_name
                product.category = category
                product.price = price
                product.stock = stock
                product.supplier_id = supplier.id
                product.update_date = datetime.now()
                session.commit()
                logging.info("Product updated: %s", product_name)
            else:
                logging.info("No changes for product: %s", product_name)
        else:
            try:
                product = Product(
                    code=product_code,
                    name=product_name,
                    category=category,
                    price=price,
                    stock=stock,
                    supplier_id=supplier.id
                )
                session.add(product)
                session.commit()
                logging.info("Product added: %s", product_name)
            except Exception as e:
                logging.error("Error adding product %s: %s", product_name, e)

@app.function_name(name="BlobTrigger")
@app.blob_trigger(arg_name="myblob", 
                  path="container1/{name}.csv",
                  connection="AzureWebJobsStorage")
def process_blob(myblob: func.InputStream) -> None:
    """
    Azure function triggered by a blob upload to process the CSV file and update the database.

    Args:
        myblob (func.InputStream): Input stream from the uploaded blob.
    """
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes")

    session = get_database_session()
    file_content = codecs.iterdecode(myblob, 'utf-8')
    process_csv(file_content, session)

    try:
        session.commit()
        logging.info("Data processed successfully.")
    except Exception as e:
        logging.error("Error processing data: %s", e)
    finally:
        session.close()
