from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError


def create_connection():
    # Connection string in SQLAlchemy format
    connection_string = "postgresql+psycopg2://kamal:kamal@localhost/fast_lms"

    try:
        # Create a SQLAlchemy engine
        engine = create_engine(connection_string)

        # Connect to the database
        connection = engine.connect()
        print("Connection to PostgreSQL DB successful")

        return connection

    except OperationalError as e:
        print(f"An error occurred: {e}")
        return None


def test_query(connection):
    try:
        # Wrap the raw SQL query in text()
        result = connection.execute(text("SELECT version();"))
        version = result.fetchone()
        print(f"PostgreSQL version: {version}")

    except Exception as e:
        print(f"An error occurred during query: {e}")


if __name__ == "__main__":
    connection = create_connection()
    if connection:
        test_query(connection)
        connection.close()
