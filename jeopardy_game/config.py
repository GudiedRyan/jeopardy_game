import os

class Config:
    SECRET_KEY= os.environ.get('JG_SECRET_KEY')