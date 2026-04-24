from __future__ import annotations

from typing import Dict

from app.core.config import DATA_ROOT
from app.utils.file_store import now_id, read_json, write_text


def generate_report(payload: Dict[str, str]) -> Dict[str, str]:
    report_id = now_id()
    student = payload["student"]
    mastery_path = DATA_ROOT / "student_profile" / "mastery_records" / f"{student}.json"
    mastery = read_json(mastery_path, default={}) or {}

    weak = [k for k, v in mastery.items() if int(v.get("score", 0)) < 75]
    good = [k for k, v in mastery.items() if int(v.get("score", 0)) >= 75]

    summary = f"当前共跟踪 {len(mastery)} 个知识点，其中薄弱/不稳定知识点 {len(weak)} 个。"

    md = f"""# 学习掌握情况报告\n\n- 学生：{student}\n- 学科：{payload['subject']}\n- 年级：{payload['grade']}\n- 报告编号：{report_id}\n\n## 一、总体结论\n\n{summary}\n\n## 二、知识点掌握情况\n\n"""
    if mastery:
        for point, item in mastery.items():
            md += f"- {point}：{item.get('score')} 分，{item.get('level')}\n"
    else:
        md += "暂无掌握度数据，请先录入错题。\n"

    md += "\n## 三、薄弱知识点\n\n"
    if weak:
        for point in weak:
            md += f"- {point}\n"
    else:
        md += "暂无明显薄弱点。\n"

    md += "\n## 四、学习建议\n\n"
    md += "1. 先复习薄弱知识点对应教材内容。\n"
    md += "2. 每个薄弱点完成 5-10 道基础题。\n"
    md += "3. 对重复出错知识点进行专项训练。\n"
    md += "4. 一周后重新生成报告，观察掌握度变化。\n"

    report_path = DATA_ROOT / "student_profile" / "reports" / f"{report_id}.md"
    write_text(report_path, md)
    return {"report_id": report_id, "report_path": str(report_path), "summary": summary}
