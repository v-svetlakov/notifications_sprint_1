from pydantic import BaseSettings, AnyUrl


class RabbitMQSettings(BaseSettings):
    USERNAME: str = 'rabbit'
    PASSWORD: str = 'rabbit'
    HOST: str = 'rabbitmq'
    PORT: int = 5672
    DSN: AnyUrl = f"amqp://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/%2F"
    EXCHANGE: str = ''
    ROUTING: str = 'welcome'

    class Config:
        env_prefix = "NOTIFIC_RABBIT_"


class PostgresSettings(BaseSettings):
    USERNAME: str = 'postgres'
    PASSWORD: str = 'password'
    HOST: str = 'db'
    PORT: int = 5432
    DB: str = 'movies'
    DSN: str = f'postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB}'

    class Config:
        env_prefix = "NOTIFIC_POSTGRES_"


class Base(BaseSettings):
    PROJECT_NAME: str = 'RabbitService'
    BITLY_ACCESS_TOKEN: str
    SENTRY_DSN: str = 'NOTIFIC_SENTRY_DSN'
    POSTGRES: PostgresSettings = PostgresSettings()
    RABBIT: RabbitMQSettings = RabbitMQSettings()
    REDIRECT_URL: str = 'http://localhost/'

    class Config:
        env_file = '.env'
