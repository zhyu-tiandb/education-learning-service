# 教育学习助手系统 API 接口设计

## 1. 基础说明

接口前缀：

```text
/api/v1
```

返回格式统一：

```json
{
  "success": true,
  "data": {},
  "message": "",
  "error_code": ""
}
```

## 2. 系统接口

### 2.1 健康检查

```http
GET /api/v1/system/health
```

返回：

```json
{
  "success": true,
  "data": {
    "status": "ok",
    "version": "v1.0.0"
  }
}
```

## 3. 教材接口

### 3.1 创建教材

```http
POST /api/v1/textbooks
```

请求：

```json
{
  "name": "人教版二年级数学上册",
  "subject": "数学",
  "grade": "二年级",
  "publisher": "人民教育出版社",
  "volume": "上册"
}
```

返回：

```json
{
  "success": true,
  "data": {
    "textbook_id": "tb_001"
  }
}
```

### 3.2 上传教材图片

```http
POST /api/v1/textbooks/{textbook_id}/pages/upload
```

请求：

```text
multipart/form-data
file: image
chapter: 可选
page_no: 可选
```

返回：

```json
{
  "success": true,
  "data": {
    "page_id": "page_001",
    "job_id": "job_001"
  }
}
```

### 3.3 处理教材页面

```http
POST /api/v1/textbooks/pages/{page_id}/process
```

返回：

```json
{
  "success": true,
  "data": {
    "job_id": "job_002"
  }
}
```

### 3.4 查询教材知识点

```http
GET /api/v1/textbooks/{textbook_id}/knowledge
```

返回：

```json
{
  "success": true,
  "data": {
    "knowledge_points": []
  }
}
```

## 4. OCR接口

### 4.1 单图片OCR

```http
POST /api/v1/ocr/image
```

请求：

```text
multipart/form-data
file: image
```

返回：

```json
{
  "success": true,
  "data": {
    "text": "OCR识别结果",
    "blocks": [],
    "confidence": 0.91
  }
}
```

## 5. 作业/错题接口

### 5.1 上传作业图片

```http
POST /api/v1/homework/upload
```

请求：

```text
multipart/form-data
file: image
student_id: stu_001
subject: 数学
```

返回：

```json
{
  "success": true,
  "data": {
    "homework_id": "hw_001",
    "job_id": "job_003"
  }
}
```

### 5.2 分析作业

```http
POST /api/v1/homework/{homework_id}/analyze
```

返回：

```json
{
  "success": true,
  "data": {
    "analysis_id": "analysis_001",
    "wrong_questions": []
  }
}
```

### 5.3 查询错题列表

```http
GET /api/v1/wrong-questions?student_id=stu_001&subject=数学
```

返回：

```json
{
  "success": true,
  "data": {
    "items": []
  }
}
```

### 5.4 更新错因标签

```http
PUT /api/v1/wrong-questions/{wrong_question_id}/error-type
```

请求：

```json
{
  "error_type": "审题错误",
  "manual_note": "家长人工修正"
}
```

## 6. 知识点接口

### 6.1 搜索知识点

```http
GET /api/v1/knowledge/search?q=小数乘法
```

返回：

```json
{
  "success": true,
  "data": {
    "items": []
  }
}
```

### 6.2 查询知识点详情

```http
GET /api/v1/knowledge/{knowledge_point_id}
```

## 7. 掌握度接口

### 7.1 查询学生掌握度

```http
GET /api/v1/mastery?student_id=stu_001&subject=数学
```

返回：

```json
{
  "success": true,
  "data": {
    "student_id": "stu_001",
    "subject": "数学",
    "knowledge_mastery": []
  }
}
```

### 7.2 重新计算掌握度

```http
POST /api/v1/mastery/recalculate
```

请求：

```json
{
  "student_id": "stu_001",
  "subject": "数学"
}
```

## 8. 报告接口

### 8.1 生成学习报告

```http
POST /api/v1/reports/generate
```

请求：

```json
{
  "student_id": "stu_001",
  "subject": "数学",
  "period": "weekly",
  "format": "markdown"
}
```

返回：

```json
{
  "success": true,
  "data": {
    "report_id": "report_001",
    "report_path": "data/reports/report_001.md"
  }
}
```

### 8.2 下载报告

```http
GET /api/v1/reports/{report_id}/download
```

## 9. 任务接口

### 9.1 查询任务状态

```http
GET /api/v1/jobs/{job_id}
```

返回：

```json
{
  "success": true,
  "data": {
    "job_id": "job_001",
    "status": "RUNNING",
    "progress": 60,
    "message": "正在进行OCR识别"
  }
}
```

## 10. V1接口验收标准

1. 所有上传接口能保存原始文件。
2. 所有处理接口能返回 job_id。
3. job 状态可查询。
4. OCR结果可查询。
5. 错题分析结果可查询。
6. 报告可生成并下载。
