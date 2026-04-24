from __future__ import annotations

from typing import Dict, List

from app.core.config import CONFIG, DATA_ROOT
from app.utils.file_store import read_json, write_json


def mastery_file(student: str) -> str:
    safe_name = student.replace("/", "_").replace("\\", "_")
    return str(DATA_ROOT / "student_profile" / "mastery_records" / f"{safe_name}.json")


def score_level(score: int) -> str:
    if score >= 90:
        return "掌握良好"
    if score >= 75:
        return "基本掌握"
    if score >= 60:
        return "不稳定"
    if score >= 40:
        return "薄弱"
    return "未掌握"


def update_mastery(student: str, knowledge_points: List[str], is_wrong: bool) -> Dict[str, Dict[str, int | str]]:
    path = DATA_ROOT / "student_profile" / "mastery_records" / f"{student}.json"
    profile = read_json(path, default={}) or {}
    rules = CONFIG.get("mastery", {})
    initial = int(rules.get("initial_score", 75))
    wrong_penalty = int(rules.get("wrong_penalty", 5))
    correct_bonus = int(rules.get("correct_bonus", 2))

    for point in knowledge_points:
        old = int(profile.get(point, {}).get("score", initial))
        new_score = old - wrong_penalty if is_wrong else old + correct_bonus
        new_score = max(0, min(100, new_score))
        profile[point] = {"score": new_score, "level": score_level(new_score)}

    write_json(path, profile)
    return profile
