import os

def get_dbconn(): os.getenv("DBCONN", "dbname=riichi user=postgres password=admin")  # Default value if not set
