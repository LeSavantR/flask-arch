from os.path import join, dirname, exists
from dotenv import load_dotenv


dotenv_file_path = join(dirname(__file__), '.env')


if exists(dotenv_file_path):
    load_dotenv(dotenv_file_path)


class Config:
    SQLALCHEMY_TRACK_MODIFICATION: bool = False


class DevelopmentConfig(Config):
    ENV: str = 'development'
    SQLALCHEMY_DATABASE_URI: str = 'sqlite:///data.db'


class ProductionConfig(Config):
    pass