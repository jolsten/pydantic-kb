import pathlib
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    library: pathlib.Path = pathlib.Path(__name__).parent / 'library'

def load_settings() -> Settings:
    return Settings()
