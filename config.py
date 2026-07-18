import os
from dotenv import load_dotenv

load_dotenv()

IBM_API_KEY = os.getenv("IBM_API_KEY")
IBM_PROJECT_ID = os.getenv("IBM_PROJECT_ID")
IBM_URL = os.getenv("IBM_URL")
IBM_MODEL_ID = os.getenv("IBM_MODEL_ID")

print("IBM_API_KEY Loaded:", IBM_API_KEY is not None)
print("IBM_PROJECT_ID:", IBM_PROJECT_ID)
print("IBM_URL:", IBM_URL)
print("IBM_MODEL_ID:", IBM_MODEL_ID)