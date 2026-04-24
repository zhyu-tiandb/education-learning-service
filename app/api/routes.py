from __future__ import annotations

from fastapi import APIRouter

from app.models.schemas import (
    ReportRequest,
    ReportResponse,
    TextbookIngestRequest,
    TextbookIngestResponse,
    WrongQuestionRequest,
    WrongQuestionResponse,
)
from app.services.report_service import generate_report
from app.services.textbook_service import ingest_textbook
from app.services.wrong_question_service import analyze_wrong_question

router = APIRouter(prefix="/api/v1")


@router.post("/textbook/ingest-text", response_model=TextbookIngestResponse)
def ingest_textbook_text(req: TextbookIngestRequest):
    return ingest_textbook(req.model_dump())


@router.post("/wrong-question/analyze", response_model=WrongQuestionResponse)
def analyze_wrong_question_api(req: WrongQuestionRequest):
    return analyze_wrong_question(req.model_dump())


@router.post("/report/generate", response_model=ReportResponse)
def generate_report_api(req: ReportRequest):
    return generate_report(req.model_dump())
