# API 使用说明

## 1. 启动服务

```bash
uvicorn app.main:app --host 127.0.0.1 --port 18080 --reload
```

## 2. Swagger 文档

```text
http://127.0.0.1:18080/docs
```

## 3. 教材学习

```bash
curl -X POST http://127.0.0.1:18080/api/v1/textbook/ingest-text \
  -H "Content-Type: application/json" \
  -d '{"subject":"数学","grade":"五年级","book":"人教版五年级上册","chapter":"小数乘法","content":"小数乘整数，先按照整数乘法计算，再根据小数位数确定小数点位置。"}'
```

## 4. 错题分析

```bash
curl -X POST http://127.0.0.1:18080/api/v1/wrong-question/analyze \
  -H "Content-Type: application/json" \
  -d '{"student":"孩子A","subject":"数学","grade":"五年级","question":"2.5 x 4 = ?","student_answer":"1.00","correct_answer":"10","chapter":"小数乘法"}'
```

## 5. 生成报告

```bash
curl -X POST http://127.0.0.1:18080/api/v1/report/generate \
  -H "Content-Type: application/json" \
  -d '{"student":"孩子A","subject":"数学","grade":"五年级"}'
```
