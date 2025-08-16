import mysql.connector
from mysql.connector import Error


try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Monubi@11350"
    )
    
    if connection.is_connected():
        cursor = connection.cursor()
        
        cursor.execute("CREATE DATABASE IF N0T EXISTS alx_book_store")
        print("DATABASE 'alx_book_store' created successfully!")
        
except Error as e:
    print(f"Error: {e}")
    
finally:
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        
    
    
        
# by use of a context manager
"""
try:
    # Use context manager for the connection
    with mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password"  # change to your actual password
    ) as connection:

        # Use context manager for the cursor
        with connection.cursor() as cursor:
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error: {e}")
"""