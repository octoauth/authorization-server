from dataclasses import dataclass
from datetime import timedelta
from typing import List


def file_content(filename) -> str:
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


@dataclass
class Settings:
    API_TITLE: str
    API_DESCRIPTION: str
    API_VERSION: str
    API_TAGS_METADATA: List[dict]

    ACCESS_TOKEN_EXPIRES: timedelta
    ACCESS_TOKEN_PRIVATE_KEY: str
    ACCESS_TOKEN_PUBLIC_KEY: str

    DATABASE_URI: str

    MAILING_ENABLED: bool
    SMTP_HOST: str
    SMTP_PORT: int
    SMTP_USERNAME: str
    SMTP_PASSWORD: str

    AUTHORIZATION_CODE_EXPIRES: timedelta
    SESSION_COOKIE_LIFETIME: timedelta


DEVELOPMENT_SETTINGS = Settings(
    API_TITLE="OctoAuth API",
    API_DESCRIPTION=("Custom SSO inspired from OIDC that exposes account management Rest services."),
    API_VERSION="0.0.1",
    API_TAGS_METADATA=[
        {"name": "accounts", "description": "Manage user account."},
        {"name": "groups", "description": "Manage groups and memberships."},
    ],
    DATABASE_URI="sqlite:///assets/database.sqlite",
    ACCESS_TOKEN_EXPIRES=timedelta(minutes=15),
    ACCESS_TOKEN_PRIVATE_KEY=file_content("assets/private-key.pem"),
    ACCESS_TOKEN_PUBLIC_KEY=file_content("assets/public-key.pem"),
    MAILING_ENABLED=False,
    SMTP_HOST="smtp.gmail.com",
    SMTP_PORT=587,
    SMTP_USERNAME="python27bot@gmail.com",
    SMTP_PASSWORD="bcvpeehtvxoixmao",
    AUTHORIZATION_CODE_EXPIRES=timedelta(seconds=15),
    SESSION_COOKIE_LIFETIME=timedelta(days=30),
)


SETTINGS = DEVELOPMENT_SETTINGS