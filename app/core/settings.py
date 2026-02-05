from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    APP_PORT: int 
    APP_HOST: str 
    APP_HASH_ALGORITHM: str 
    APP_SECRET_KEY: str
    APP_ENCODE_ALGORITHM: str
    APP_ACCESS_TOKEN_EXPIRE_MINUTES: int


class DatabaseSettings(BaseSettings):
    POSTGRES_DB: str 
    POSTGRES_USER: str  
    POSTGRES_PASSWORD: str  
    POSTGRES_PORT: int 
    POSTGRES_HOST: str 

    def database_url(self):
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"


class CacheSettings():
    REDIS_HOST: str 
    REDIS_PORT: int 
    REDIS_PASSWORD: str
    REDIS_EXP: int


class Settings(
    AppSettings,
    DatabaseSettings,
    CacheSettings
):
    model_config = SettingsConfigDict(env_file=".env")
    

settings = Settings()