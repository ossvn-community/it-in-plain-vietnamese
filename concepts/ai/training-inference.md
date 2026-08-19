---
title: "Training và Inference là gì?"
category: "ai"
core: true
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# Training và Inference là gì?

**Training** là giai đoạn model học từ dữ liệu bằng cách điều chỉnh các tham số của nó.

**Inference** là giai đoạn dùng model đã được training để xử lý input mới và tạo ra kết quả. Hai khái niệm này tương ứng gần với “học” và “đem phần đã học ra sử dụng”.

## Nó hoạt động thế nào?

Một flow đơn giản:

```text
Training data
    ↓
 Training
    ↓
  Model
    ↓
Input mới
    ↓
Inference
    ↓
 Output
```

Training và inference là hai giai đoạn khác nhau. Một model thường được training trước rồi mới được dùng nhiều lần cho inference.

## Ví dụ

Với một model nhận diện ảnh:

- Training: model học từ nhiều ảnh trong dữ liệu training.
- Inference: đưa một ảnh mới vào model và nhận kết quả phân loại.

Với LLM, inference có thể là đưa prompt vào model đã training để sinh response.

## Đọc tiếp

- [Model](model.md)
- [Dataset](dataset.md)
- [Large Language Model](large-language-model.md)

## Nguồn

- [NIST CSRC Glossary - Training Stage](https://csrc.nist.gov/glossary/term/training_stage)
- [NIST AI 100-2 E2025 - Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations](https://csrc.nist.gov/pubs/ai/100/2/e2025/final)
- [Google for Developers - Machine Learning Glossary: Training and Inference](https://developers.google.com/machine-learning/glossary/fundamentals)
