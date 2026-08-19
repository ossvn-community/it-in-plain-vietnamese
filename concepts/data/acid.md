---
title: "ACID là gì?"
category: "data"
core: false
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# ACID là gì?

ACID là bốn nhóm thuộc tính thường dùng để mô tả độ tin cậy của transaction trong database: Atomicity, Consistency, Isolation và Durability.

Nó giúp nói rõ database cần đảm bảo điều gì khi nhiều thao tác dữ liệu xảy ra, kể cả khi có lỗi hoặc nhiều transaction chạy đồng thời.

## Ví dụ

Với giao dịch chuyển tiền:
- **Atomicity**: không để chỉ trừ mà chưa cộng.
- **Consistency**: các quy tắc dữ liệu vẫn được giữ.
- **Isolation**: transaction đồng thời không nhìn thấy trạng thái dở dang theo mức isolation được chọn.
- **Durability**: sau khi commit, kết quả phải được lưu bền vững theo cam kết của hệ thống.

## Dễ nhầm với gì?

ACID không có nghĩa database không bao giờ mất dữ liệu trong mọi sự cố. Mức đảm bảo cụ thể còn phụ thuộc cấu hình, storage và hệ quản trị.

## Nguồn

- [PostgreSQL Documentation - Transactions](https://www.postgresql.org/docs/current/tutorial-transactions.html)
- [PostgreSQL Documentation - Transaction Isolation](https://www.postgresql.org/docs/current/transaction-iso.html)
