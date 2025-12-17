from pydantic_settings import BaseSettings

class Settings(BaseSettings):
  APP_NAME: str = "TaskForge API"
  ENVIRONMENT: str = "development"
  DATABASE_URL: str | None = None
  
  class Config:
    env_file = ".env"
    
settings = Settings()