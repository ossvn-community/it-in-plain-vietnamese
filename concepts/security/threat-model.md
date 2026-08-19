---
title: "Threat Model là gì?"
category: "security"
core: false
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# Threat Model là gì?

Threat Model - mô hình mối đe dọa - là cách có hệ thống để xác định thứ cần bảo vệ, ai hoặc điều gì có thể gây hại, các đường tấn công có thể xảy ra và biện pháp giảm rủi ro.

Nó giúp đội phát triển suy nghĩ về security trước khi chỉ phản ứng với bug sau khi sản phẩm đã chạy.

## Ví dụ

Với ứng dụng lưu ảnh riêng tư, threat model có thể hỏi:
- dữ liệu nào nhạy cảm;
- ai được phép truy cập;
- attacker có thể lấy token bằng cách nào;
- dữ liệu đi qua những service nào;
- cần kiểm soát nào ở từng điểm.

## Dễ nhầm với gì?

Threat Model không phải danh sách tất cả vulnerability đã biết. Nó là mô hình về tài sản, tác nhân, trust boundary và các kịch bản đe dọa.

## Nguồn

- [NIST CSRC Glossary - Threat Modeling](https://csrc.nist.gov/glossary/term/threat_modeling)
