from dotenv import load_dotenv
import os

load_dotenv()

config = {
  # database postgres config
  "POSTGRES_DBNAME" : os.getenv('POSTGRES_DBNAME') ,
  "POSTGRES_DBUSER" : os.getenv('POSTGRES_DBUSER') ,
  "POSTGRES_DBPASSWORD" : os.getenv('POSTGRES_DBPASSWORD') ,
  "POSTGRES_DBHOST" : os.getenv('POSTGRES_DBHOST') ,
  "POSTGRES_DBPORT" : os.getenv('POSTGRES_DBPORT') ,
}
