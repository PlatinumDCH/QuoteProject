from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    uri_mongodb :str = 'stringa'

    pg_database_name : str = 'test'
    pg_user :str = 'test'
    pg_password : str = 'test' 
    pg_host : str = 'localhost'
    pg_port : str = '5432'

    SECRET_KEY :str = 'str'
    
    model_config = SettingsConfigDict(
        extra="ignore", 
        env_file=".env", 
        env_file_encoding="utf-8"
    )


settings = Settings()