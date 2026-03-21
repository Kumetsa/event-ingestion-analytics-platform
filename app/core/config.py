from pydantic_settings import BaseSettings, SettingsConfigDict

"""
This file contains the configuration for the application.
"""



class Settings(BaseSettings):
    app_name: str = "Event Ingestion & Analytics Platform"
    app_env: str = "development"

    db_host: str = "localhost"
    db_port: int = 5433
    db_name: str = "event_platform"
    db_user: str = "postgres"
    db_password: str = "1235"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


settings = Settings()