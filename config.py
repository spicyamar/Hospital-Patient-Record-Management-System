import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/hospital_db')
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', os.path.join(os.path.dirname(__file__), 'static', 'images'))
    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
