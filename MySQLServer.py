import mysql.connector

def create_database():
    try:
        # Connect to MySQL Server (empty password)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""  # Empty password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error while connecting to MySQL: {err}")

    finally:
        # Close connection if open
        try:
            if connection.is_connected():
                cursor.close()
                connection.close()
        except NameError:
            pass  # connection variable not defined if connection failed

if __name__ == "__main__":
    create_database()
