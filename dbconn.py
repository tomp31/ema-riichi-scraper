import os

def get_dbconn(): 
    return os.getenv("DBCONN", "dbname=riichi user=postgres password=admin")  # Default value if not set
