from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    SECRET_KEY: SecretStr
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    max_upload_size: int = 5 * 1024 * 1024  # 5 MB
    posts_per_page: int = 10

    rest_token_expire_minutes: int = 15
    mail_server: str = 'localhost'
    mail_port: int = 587
    mail_username: str = ''
    mail_password: SecretStr = SecretStr('')
    mail_from: str = 'noreply@gmail.com'
    mail_use_tls: bool = True

    frontend_url: str = 'http://localhost:8000'


settings = Settings()   