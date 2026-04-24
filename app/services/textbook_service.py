from __future__ import annotations

from pathlib import Path
from typing import Dict, List

from app.core.config import DATA_ROOT
from app.utils.file_store import now_id, write_json, write_text


def extract_knowledge_points(content: str, chapter: str) -> List[str]:
    # V1 Stub：后续替换为大模型/规则/知识图谱抽取
    points = []
    if "小数" in content:
        points.append("小数计算")
    if "乘" in content:
        points.append("乘法运算")
    if "小数点" in content:
        points.append("小数点位置判断")
    if not points:
        points.append(chapter)
    return sorted(set(points))


def ingest_textbook(payload: Dict[str, str]) -> Dict[str, str | List[str]]:
    record_id = now_id()
    points = extract_knowledge_points(payload["content"], payload["chapter"])
    data = {
        "record_id": record_id,
        "subject": payload["subject"],
        "grade": payload["grade"],
        "book": payload["book"],
        "chapter": payload["chapter"],
        "content": payload["content"],
        "knowledge_points": points,
        "common_mistakes": ["概念理解不到位", "计算步骤不完整", "小数点位置判断错误"],
        "source": "text_input_v1"
    }

    json_path = DATA_ROOT / "knowledge" / "textbook_knowledge" / f"{record_id}.json"
    md_path = DATA_ROOT / "knowledge" / "textbook_knowledge" / f"{record_id}.md"
    write_json(json_path, data)

    md = f"""# 教材知识记录\n\n- 学科：{payload['subject']}\n- 年级：{payload['grade']}\n- 教材：{payload['book']}\n- 章节：{payload['chapter']}\n\n## 知识点\n\n""" + "\n".join([f"- {p}" for p in points]) + f"""\n\n## 原始内容\n\n{payload['content']}\n"""
    write_text(md_path, md)
    return {"record_id": record_id, "knowledge_points": points, "saved_path": str(json_path)}
