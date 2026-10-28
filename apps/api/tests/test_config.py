from app.core.config import get_settings


def test_application_settings() -> None:
    settings = get_settings()

    assert settings.app_name == "invikost"
    assert settings.app_version == "2.0.0"
    assert settings.database_url
    assert settings.redis_url