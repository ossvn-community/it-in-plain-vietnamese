---
title: "Relational Database là gì?"
category: "data"
core: false
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# Relational Database là gì?

Relational Database - cơ sở dữ liệu quan hệ - tổ chức dữ liệu thành các table và cho phép các table liên hệ với nhau thông qua các giá trị khóa.

Mô hình này phù hợp khi dữ liệu có cấu trúc rõ và các quan hệ giữa bản ghi quan trọng.

## Tại sao cần nó?

Relational model là nền tảng của nhiều database system phổ biến và là context chính khi bạn học SQL, table, key và index.

Nếu mới bắt đầu, chỉ cần hiểu structure cơ bản trước khi học normalization hoặc database theory sâu hơn.

## Ví dụ

Một hệ thống bán hàng có thể có:

```text
users
orders
products
```

Các table lưu những loại record khác nhau. Column như `user_id` có thể được dùng để thể hiện quan hệ giữa order và user, thường kết hợp với key/constraint.

## Dễ nhầm với gì?

**Relational Database không đồng nghĩa với mọi Database.** Có nhiều mô hình database khác ngoài relational.

**Relation trong lý thuyết relational không hoàn toàn chỉ là bảng hiển thị trên màn hình**, nhưng ở level beginner có thể bắt đầu bằng cách hiểu table là representation thực tế thường gặp.

## Đọc tiếp

- [Table, Row và Column là gì?](table-row-column.md)
- [SQL là gì?](sql.md)
- [Primary Key là gì?](primary-key.md)

## Nguồn

- [PostgreSQL Documentation - Concepts](https://www.postgresql.org/docs/current/tutorial-concepts.html)
