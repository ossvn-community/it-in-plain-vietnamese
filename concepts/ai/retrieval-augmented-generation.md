---
title: "Retrieval-Augmented Generation là gì?"
category: "ai"
core: false
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# Retrieval-Augmented Generation là gì?

Retrieval-Augmented Generation - thường viết tắt là **RAG** - là cách kết hợp một model sinh nội dung với bước tìm kiếm thông tin liên quan từ nguồn dữ liệu bên ngoài.

Thông tin được lấy ra được đưa vào context để model tạo câu trả lời dựa trên dữ liệu đó thay vì chỉ dựa vào những gì model đã học khi training.

## Ví dụ

Một chatbot nội bộ nhận câu hỏi về quy định công ty. Hệ thống tìm các đoạn liên quan trong tài liệu nội bộ rồi đưa chúng cùng câu hỏi vào LLM để tạo câu trả lời.

## Dễ nhầm với gì?

RAG không đảm bảo câu trả lời luôn đúng. Chất lượng còn phụ thuộc dữ liệu nguồn, cách retrieval, context được chọn và cách model sử dụng context.

## Nguồn

- [Lewis et al. - Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401)
