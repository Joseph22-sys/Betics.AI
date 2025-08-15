import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

basedir = Path(__file__).resolve().parent

#Model Path inside app/model/logistic_models

model_path = basedir / "app" / "model" / "logistic_models" / "diabetes_model.pkl"
scaler_path = basedir / "app" / "model" / "logistic_models" / "scaler.pkl"


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')\
        or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
