from dotenv import load_dotenv
import os

load_dotenv('.env')

DJANGO_SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")