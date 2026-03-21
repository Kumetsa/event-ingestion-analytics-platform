from fastapi import FastAPI

app = FastAPI(title="Event Ingestion & Analytics Platform")


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Event Ingestion & Analytics Platform"}


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}