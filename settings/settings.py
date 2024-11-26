from dotenv import load_dotenv
import os

load_dotenv()

config = {
    "DB_NAME" : os.getenv('DBNAME') ,
    "DB_USER" : os.getenv('DBUSER') ,
    "DB_PASSWORD" : os.getenv('DBPASSWORD') ,
    "DB_HOST" : os.getenv('DBHOST') ,
    "DB_PORT" : os.getenv('DBPORT') ,
}
