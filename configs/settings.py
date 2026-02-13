"""
Configuration settings for the ETL pipeline.

This module centralizes all configuration:
- Database connection parameters
- File paths
- Table mappings
- Validation rules
- Environment-specific settings

Environment variables are loaded from .env file.
"""

import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

# Get appropriate log_level per environment
ENVIRONMENT = os.getenv('ENVIRONMENT', 'dev').lower()
if ENVIRONMENT == 'dev':
    log_level = 'DEBUG' # capoture everything
elif ENVIRONMENT in ('uat', 'prod'):
    log_level = 'INFO' # less noisy
else:
    log_level = 'INFO' # default

# Postgres connection string  
POSTGRES_CONNECTION_STRING =  {
    'dbname': 'dwh',
    'user': 'postgres',
    'host': 'localhost',
    'port': 5432,
    'password': os.environ.get('POSTGRES_PASSWORD')
}

# Schema names
SCHEMA_NAMES = {
    'staging': 'staging',
    'final': 'final'
}


# Get the project root directory
# config -> load_csv_to_db
PROJECT_ROOT = Path(__file__).parent.parent

# Define data directories
DATA_DIR = PROJECT_ROOT / 'data'
RAW_DATA_DIR = DATA_DIR / 'raw'
PROCESSED_DATA_DIR = DATA_DIR / 'processed'
FAILED_DATA_DIR = DATA_DIR / 'failed'
LOGS_DIR = PROJECT_ROOT / 'logs'

# Mapping tables
TABLES = {
    'customers': {
        'source_file': 'customers.csv',
        'staging_table': 'staging.customers',
        'final_table': 'final.customers',
        'primary_key': 'customer_id',
        'required_columns': ['customer_id', 'customer_unique_id']
    },
    'orders': {
        'source_file': 'orders.csv',
        'staging_table': 'staging.orders',
        'final_table': 'final.orders',
        'primary_key': 'order_id',
        'required_columns': ['order_id', 'customer_id']
    },
    'products': {
        'source_file': 'products.csv',
        'staging_table': 'staging.products',
        'final_table': 'final.products',
        'primary_key': 'product_id',
        'required_columns': ['product_id']
    }
}

# Data Validation Rules
VALIDATION_RULES = {
    'customers': {
        'null_checks': ['customer_id', 'customer_unique_id'],
        'duplicate_check': 'customer_id',
        'max_null_percentage': 0.01
    },
    'orders': {
        'null_checks': ['order_id', 'customer_id'],
        'duplicate_check': 'order_id',
        'max_null_percentage': 0.05
    },
    'products': {
        'null_checks': ['product_id'],
        'duplicate_check': 'product_id',
        'max_null_percentage': 0.02
    }
}