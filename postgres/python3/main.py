import psycopg2
from psycopg2 import RealDictCursor
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

class PostgreSQLClient:
    def __init__(self, host, port, database, user, password):
        self.connection_params = {
            'host': host,
            'port': port,
            'database': database,
            'user': user,
            'password': password
        }
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(**self.connection_params)
            logger.info("PostgreSQL connection established.")
        except Exception as e:
            logger.error(f"Error connecting to PostgreSQL: {e}")

    def close(self):
        if self.connection:
            self.connection.close()
            logger.info("PostgreSQL connection closed.")

    def execute_query(self, query, params=None):
        if not self.connection:
            logger.error("No active PostgreSQL connection.")
            return None
        try:
            with self.connection.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(query, params)
                results = cursor.fetchall()
                logger.info(f"Query executed successfully: {query}")
                return results
        except Exception as e:
            logger.error(f"Error executing query: {e}")
            return None
        
# Example usage
def main():
    # Initialize client
    db = PostgreSQLClient(
        host="localhost",
        port=5432,
        database="testdb",
        user="postgres",
        password="password"
    )
    
    # Connect to database
    if not db.connect():
        return
    
    try:
        # Query data
        select_query = "SELECT * FROM users WHERE name = %s"
        results = db.execute_query(select_query, ("John Doe",))
        
        if results:
            for row in results:
                logger.info(f"User: {row['name']}, Email: {row['email']}")
    
    finally:
        db.close()

if __name__ == "__main__":
    main()