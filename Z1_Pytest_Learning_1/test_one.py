from datetime import date
import pytest
from datetime import datetime


def get_date() -> date:
    """
    Return the current date.

    Returns:
        date: The current date as a `datetime.date` object.
    """
    return date.today()


# Use the fixture in a test class
class TestSomething:
    date = None  # Class attribute to hold the date

    @classmethod
    def setup_class(cls):
        # Get the current date using the fixture
        pass
 
def execute_delete_statements(delete_statements):
    """
    Execute multiple delete statements and return the result.

    Args:
        delete_statements (list): List of delete statements with conditions.

    Returns:
        bool: True if all delete statements are successful, False otherwise.
    """
    # Establish a connection to the database
    conn = pyodbc.connect("your_connection_string_here")

    # Create a cursor object to execute SQL statements
    cursor = conn.cursor()

    try:
        for statement in delete_statements:
            # Execute the delete statement
            cursor.execute(statement)

        # Commit the changes to the database
        conn.commit()

        # Close the cursor and connection
        cursor.close()
        conn.close()

        return True

    except Exception as e:
        print(f"Error executing delete statements: {e}")

        # Rollback the changes and close the connection
        conn.rollback()
        cursor.close()
        conn.close()

        return False
    return True