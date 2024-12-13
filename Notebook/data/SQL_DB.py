import sys
import os
from urllib.parse import quote_plus
import pandas as pd
from sqlalchemy import create_engine


from  src.logger import logging
from src.exception import CustomException

# MySQL connection details
USERNAME = 'root'
PASSWORD = quote_plus('Alliswell@92')  # to encode the @ symbol and password
HOST = 'localhost'     
PORT = '3306'              
DATABASE_NAME = 'gravity_books'

#use %40 to encode @ symbol to avoid considering as any part of python operation
connection_string = f'mysql+mysqlconnector://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE_NAME}'

# Function to create the database engine
def create_engine_connection():
    try:
        # Create the SQLAlchemy engine
        engine = create_engine(connection_string)
        logging.info("Successfully created engine connection")
        return engine
    except Exception as e:
        logging.info(f"Error while creating engine:{str(e)}")
        raise CustomException(e,sys)
    
# Function to fetch table data.  
def fetch_table_data(engine,table_name):
    try:
        with engine.connect() as connection:
            logging.info(f"Fetching data for table: {table_name}")
            return pd.read_sql_query(f"SELECT * FROM {table_name}",connection)
    except Exception as e:
        logging.info("Error while fetch the table data for :{table_name}")
        raise CustomException(e, sys)

def save_data_to_csv(dataframe,sub_folder,file_name):
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        folder_path = os.path.join(base_dir,sub_folder)
        os.makedirs(folder_path,exist_ok=True)
        file_path = os.path.join(folder_path,file_name)
        
        if os.path.exists(file_path):
            raise CustomException(f"The file '{file_name}' already exists in '{sub_folder}'. Aborting save.",sys)
        dataframe.to_csv(file_path,index=False)
        logging.info(f"File saved as csv:{file_name}")
        
    except Exception as e:
        logging.info(f"Error raised while saving {file_name}")
        raise CustomException(e,sys)
    
    
if __name__ == '__main__':
    try:
        engine = create_engine_connection()
        # List of tables to fetch data from
        tables = ["book", "book_author", "author", "book_language", "publisher",
                  "customer", "cust_order", "customer_address", "address", 
                  "address_status", "order_history", "order_line", 
                  "order_status", "shipping_method"]
        
        sub_folder = "RAW_CSV"
        
        for table_name in tables:
            dataframe = fetch_table_data(engine,table_name)
            file_name = f"{table_name}.csv"
            
            save_data_to_csv(dataframe,sub_folder=sub_folder,file_name=file_name)    
        logging.info("Data has been saved as CSV file")
            
    except Exception as e:
        logging.info(f"An Error occured:{str(e)}")
        raise CustomException(e,sys)