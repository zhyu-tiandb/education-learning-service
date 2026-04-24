# 教育学习助手系统 OpenClaw 接入设计

## 1. 接入定位

教育学习助手系统主体应作为独立本地服务运行，OpenClaw 不直接承担 OCR、视频处理、文件管理和数据库管理。

OpenClaw 的角色是：

```text
技能调用入口
报告增强
经验沉淀
流程编排
管理分析
```

推荐架构：

```text
OpenClaw Skill
    ↓ HTTP API
本地 education-learning-service
    ↓
OCR / 错题分析 / 掌握度 / 报告
    ↓
本地知识库与学生画像
```

## 2. 为什么不直接做成 OpenClaw Skill

不建议把主体能力完全做成 Skill，原因：

1. 图片和视频处理需要稳定的服务环境。
2. OCR和ASR依赖较重，Skill中不利于调试。
3. 长期学生画像需要数据库支持。
4. 前端页面和文件管理更适合独立服务。
5. OpenClaw更适合做编排和调用。

## 3. Skill能力边界

OpenClaw Skill 应提供以下能力：

1. 调用本地服务分析教材。
2. 调用本地服务分析错题。
3. 读取学习报告。
4. 总结阶段性学习情况。
5. 生成家长辅导建议。
6. 将有效经验沉淀到 OpenClaw 本地记忆。

## 4. Skill目录结构建议

```text
education-learning-assistant-skill/
├── SKILL.md
├── config/
│   └── skill_config.json
├── prompts/
│   ├── analyze_learning_report.md
│   ├── generate_parent_advice.md
│   └── summarize_weak_points.md
├── scripts/
│   ├── call_service.py
│   ├── fetch_report.py
│   └── save_experience.py
└── docs/
    └── 使用说明.md
```

## 5. Skill调用示例

### 5.1 分析教材

```text
使用 education-learning-assistant 技能，调用本地教育学习服务分析教材图片：

教材路径：
D:\OpenClaw\education-learning\data\raw\textbook_images\

要求：
1. 上传教材图片到本地服务
2. 执行OCR和知识点提取
3. 返回知识点摘要
4. 将结果保存为本地经验
```

### 5.2 分析错题

```text
使用 education-learning-assistant 技能，分析以下错题：

路径：
D:\OpenClaw\education-learning\data\raw\homework_images\2026-04-24\

要求：
1. 调用本地服务进行错题分析
2. 读取知识点匹配结果
3. 输出薄弱点和学习建议
4. 生成家长辅导摘要
```

### 5.3 生成阶段性报告

```text
使用 education-learning-assistant 技能，读取最近一周学习报告，生成面向家长的总结：

要求：
1. 总结主要薄弱知识点
2. 总结重复错因
3. 给出下周辅导重点
4. 输出可执行学习安排
```

## 6. 本地服务API配置

```json
{
  "service_base_url": "http://127.0.0.1:18080/api/v1",
  "default_student_id": "stu_001",
  "default_subject": "数学",
  "report_dir": "D:/OpenClaw/education-learning/data/reports",
  "experience_dir": "D:/OpenClaw/memory/education-learning"
}
```

## 7. OpenClaw沉淀经验格式

建议保存为 Markdown：

```text
# 学习经验记录

## 学生
学生A

## 学科
数学

## 时间
2026-04-24

## 薄弱知识点
- 乘法意义
- 乘法口诀应用

## 重复错因
- 概念不清
- 审题错误

## 有效辅导方法
- 先回到教材例题
- 再做基础题
- 最后做变式题

## 后续建议
下周继续检测乘法意义相关题型。
```

## 8. 接入阶段

### 阶段1

本地服务先跑通，不接 OpenClaw。

### 阶段2

OpenClaw 通过 API 查询报告。

### 阶段3

OpenClaw 生成家长建议和学习计划。

### 阶段4

OpenClaw 沉淀有效辅导经验，形成长期教育经验库。

## 9. 结论

主体能力必须放在独立服务中，OpenClaw 做调用和增强。

推荐边界：

```text
本地服务负责：识别、分析、存储、报告
OpenClaw负责：调用、总结、经验沉淀、流程管理
```
