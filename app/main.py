from fastapi import FastAPI

from app.api.routes.events import router as events_router

app = FastAPI(title="Event Ingestion & Analytics Platform")

app.include_router(events_router)


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Event Ingestion & Analytics Platform"}


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}

