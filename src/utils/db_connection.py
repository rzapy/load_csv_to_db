import sys
from pathlib import Path

project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

import psycopg2
from configs.settings import POSTGRES_CONNECTION_STRING
from configs.logging_config import setup_logger
from src.utils.exceptions import LoadError

logger = setup_logger('db_connection')

def get_connection(connection_string: dict = POSTGRES_CONNECTION_STRING):
    """
    Create and return database connection
    
    Args:
        connection_string: Database connection parameters
    
    Returns:
        psycopg2 connection object
        
    Raises:
        Exception if connection fails
    """
    try:
        conn = psycopg2.connect(**connection_string)
        logger.info('Successfully connected to database')
        return conn
    except Exception as e:
        logger.critical(f'Failed to connect to database, error: {e}')
        raise LoadError(f'Database connection failed: {e}')
    


def test_connection() -> bool:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT version();')
        version = cursor.fetchone()
        logger.info(f'Database version: {version[0]}')
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        logger.error(f'Connection test failed: {e}')
        return False



if __name__ == '__main__':
    if test_connection():
        print('Database connection works!')
    else:
        print('Database connection failed')