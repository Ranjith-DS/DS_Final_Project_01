import pandas as pd
from sqlalchemy import create_engine

# MySQL connection details
username = 'root'
password = 'Alliswell@92'  
host = 'localhost'         
port = '3306'               
database_name = 'gravity_books'

#use %40 to encode @ symbol to avoide considering as any part of python operation
connection_string = f'mysql+mysqlconnector://{username}:{password.replace("@","%40")}@{host}:{port}/{database_name}'

# Create the SQLAlchemy engine
engine = create_engine(connection_string)

try:
    with engine.connect() as connection:
        print("Connection successful!")
except Exception as e:
    print(f"Error: {e}")
try:
    book_df = pd.read_sql_query("SELECT * FROM book",engine)
    book_author_df = pd.read_sql_query("SELECT * FROM book_author",engine)
    author_name_df = pd.read_sql_query("SELECT * FROM author",engine)
    book_lang_df = pd.read_sql_query("SELECT * FROM book_language",engine)
    book_publisher_df = pd.read_sql_query("SELECT * FROM publisher",engine)

    customer_df = pd.read_sql_query("SELECT * FROM customer",engine)
    customer_order_df = pd.read_sql_query("SELECT * FROM cust_order",engine)
    customer_address_id_df = pd.read_sql_query("SELECT * FROM customer_address",engine)
    customer_address_name_df = pd.read_sql_query("SELECT * FROM address",engine)
    customer_address_status_df = pd.read_sql_query("SELECT * FROM address_status",engine)

    order_history_df = pd.read_sql_query("SELECT * FROM order_history",engine)
    order_line_df = pd.read_sql_query("SELECT * FROM order_line",engine)
    order_status_df = pd.read_sql_query("SELECT * FROM order_status",engine)
    shipping_method_df = pd.read_sql_query("SELECT * FROM shipping_method",engine)
except Exception as e:
        print(f"Error on data reading: {e}")