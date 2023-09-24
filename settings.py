from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    redis_host: str
    redis_port: int

    class Config:
        env_file = ".env"

