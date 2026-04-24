from __future__ import annotations

from typing import Dict, List

from app.core.config import DATA_ROOT
from app.services.mastery_service import update_mastery
from app.utils.file_store import now_id, write_json


def match_knowledge_points(question: str, chapter: str | None) -> List[str]:
    points = []
    text = question + " " + (chapter or "")
    if "小数" in text or "." in text:
        points.append("小数计算")
    if "乘" in text or "x" in text or "×" in text:
        points.append("乘法运算")
    if "." in text:
        points.append("小数点位置判断")
    if not points and chapter:
        points.append(chapter)
    return sorted(set(points or ["未分类知识点"]))


def infer_error_type(question: str, student_answer: str, correct_answer: str) -> tuple[str, str]:
    if student_answer.strip() == correct_answer.strip():
        return "无错误", "答案与标准答案一致。"
    if "." in question and student_answer.replace(".", "").isdigit():
        return "小数点位置错误", "题目包含小数，学生答案可能存在小数点位置或位数判断错误。"
    if student_answer.isdigit() and correct_answer.isdigit():
        return "计算错误", "学生答案与标准答案不一致，初步判断为计算过程错误。"
    return "方法不会", "当前答案与标准答案不一致，需要结合解题步骤进一步确认。"


def analyze_wrong_question(payload: Dict[str, str]) -> Dict[str, object]:
    record_id = now_id()
    is_wrong = payload["student_answer"].strip() != payload["correct_answer"].strip()
    points = match_knowledge_points(payload["question"], payload.get("chapter"))
    error_type, error_reason = infer_error_type(payload["question"], payload["student_answer"], payload["correct_answer"])

    record = {
        "record_id": record_id,
        **payload,
        "is_wrong": is_wrong,
        "knowledge_points": points,
        "error_type": error_type,
        "error_reason": error_reason,
        "suggestion": "先回到教材对应知识点复习，再完成 5-10 道同类型基础题。"
    }

    path = DATA_ROOT / "student_profile" / "wrong_question_records" / f"{record_id}.json"
    write_json(path, record)
    update_mastery(payload["student"], points, is_wrong=is_wrong)

    return {
        "record_id": record_id,
        "is_wrong": is_wrong,
        "knowledge_points": points,
        "error_type": error_type,
        "error_reason": error_reason,
        "saved_path": str(path)
    }
