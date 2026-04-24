from __future__ import annotations

from typing import List, Optional
from pydantic import BaseModel, Field


class TextbookIngestRequest(BaseModel):
    subject: str = Field(..., examples=["数学"])
    grade: str = Field(..., examples=["五年级"])
    book: str = Field(..., examples=["人教版五年级上册"])
    chapter: str = Field(..., examples=["小数乘法"])
    content: str = Field(..., description="OCR 后的教材文本，V1 可直接传文本")


class TextbookIngestResponse(BaseModel):
    record_id: str
    knowledge_points: List[str]
    saved_path: str


class WrongQuestionRequest(BaseModel):
    student: str = "孩子A"
    subject: str = "数学"
    grade: str = "五年级"
    chapter: Optional[str] = None
    question: str
    student_answer: str
    correct_answer: str


class WrongQuestionResponse(BaseModel):
    record_id: str
    is_wrong: bool
    knowledge_points: List[str]
    error_type: str
    error_reason: str
    saved_path: str


class ReportRequest(BaseModel):
    student: str = "孩子A"
    subject: str = "数学"
    grade: str = "五年级"


class ReportResponse(BaseModel):
    report_id: str
    report_path: str
    summary: str
