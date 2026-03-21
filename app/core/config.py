from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Event Ingestion & Analytics Platform"
    app_env: str = "development"

    db_host: str = "localhost"
    db_port: int = 5432
    db_name: str = "event_platform"
    db_user: str = "postgres"
    db_password: str = "postgres"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


settings = Settings()