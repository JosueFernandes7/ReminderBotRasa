from dotenv import load_dotenv
import os
load_dotenv()

class Settings:
    DB_URL       = os.environ.get("DB_URL")
    DB_NAME       = os.environ.get("DB_NAME")
    DB_COLLECTION = os.environ.get("DB_COLLECTION")

settings = Settings()