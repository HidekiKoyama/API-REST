from dotenv import load_dotenv
import os

load_dotenv()

config = {
  "DBNAME" : os.getenv('DBNAME') ,
  "DBUSER" : os.getenv('DBUSER') ,
  "DBPASSWORD" : os.getenv('DBPASSWORD') ,
  "DBHOST" : os.getenv('DBHOST') ,
  "DBPORT" : os.getenv('DBPORT') ,
}
