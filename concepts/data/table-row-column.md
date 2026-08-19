---
title: "Table, Row và Column là gì?"
category: "data"
core: true
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# Table, Row và Column là gì?

Trong relational database, **table** giống một bảng dữ liệu; **row** là một bản ghi; **column** là một thuộc tính mà các row trong bảng có thể lưu.

Ba khái niệm này tạo nên cách nhìn cơ bản nhất khi bắt đầu làm việc với database dạng quan hệ.

## Ví dụ

```text
users
+----+------+-------------------+
| id | name | email             |
+----+------+-------------------+
| 1  | An   | an@example.com    |
| 2  | Binh | binh@example.com  |
+----+------+-------------------+
```

Ở đây:

- `users` là table
- mỗi dòng dữ liệu là một row
- `id`, `name`, `email` là các column

## Tại sao cần nó?

Đây là structure cơ bản để hiểu relational database và SQL.

Khi viết query, bạn thường chọn column từ table và lọc row theo điều kiện.

```sql
SELECT name, email
FROM users
WHERE id = 1;
```

## Dễ nhầm với gì?

**Row không có thứ tự mặc định đáng tin cậy trong SQL.** Nếu cần thứ tự cụ thể khi query, hãy dùng `ORDER BY`.

**Column không chỉ là tên field.** Column còn có data type và có thể có constraint.

## Đọc tiếp

- [SQL là gì?](sql.md)
- [Primary Key là gì?](primary-key.md)
- [Index là gì?](index.md)

## Nguồn

- [PostgreSQL Documentation - Concepts](https://www.postgresql.org/docs/current/tutorial-concepts.html)
- [PostgreSQL Documentation - Creating a New Table](https://www.postgresql.org/docs/current/tutorial-table.html)
