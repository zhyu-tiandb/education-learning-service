from __future__ import annotations

from fastapi import FastAPI

from app.api.routes import router
from app.core.config import CONFIG, DATA_ROOT

app = FastAPI(
    title="Education Learning Service",
    description="本地教育学习助手 V1：教材学习、错题分析、掌握度报告。",
    version=CONFIG.get("version", "1.0.0"),
)

app.include_router(router)


@app.get("/health")
def health():
    return {
        "status": "ok",
        "app": CONFIG.get("app_name"),
        "version": CONFIG.get("version"),
        "data_root": str(DATA_ROOT),
    }
