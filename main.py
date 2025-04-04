import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("example_api")

print(api_key)

