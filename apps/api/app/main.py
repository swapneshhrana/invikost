from fastapi import FastAPI

from app.core.config import get_settings

settings = get_settings()

app = FastAPI(
    title=f"{settings.app_name} API",
    description="Autonomous Cloud Efficiency & Savings Assurance",
    version=settings.app_version,
)


@app.get("/health")
def health() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "invikost-api",
        "version": settings.app_version,
    }