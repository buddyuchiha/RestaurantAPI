from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    pass 


class DatabaseSettings(BaseSettings):
    POSTGRES_DB: str 
    POSTGRES_USER: str  
    POSTGRES_PASSWORD: str  
    POSTGRES_PORT: int 
    POSTGRES_HOST: str 

    @property
    def database_url(self):
        return f"postgresql+psycopg2://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

class CacheSettings():
    pass 



class Settings(
    AppSettings,
    DatabaseSettings,
    CacheSettings
):
    model_config = SettingsConfigDict(env_file=".env")