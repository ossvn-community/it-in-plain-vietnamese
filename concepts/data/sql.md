---
title: "SQL là gì?"
category: "data"
core: true
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# SQL là gì?

SQL - Structured Query Language - là ngôn ngữ dùng để làm việc với relational database.

Bạn có thể dùng SQL để đọc, thêm, sửa, xóa dữ liệu và mô tả một phần cấu trúc của database.

## Tại sao cần nó?

SQL cho phép bạn mô tả data muốn lấy hoặc thay đổi thay vì tự viết code để duyệt từng record ở mức thấp.

Các thao tác cơ bản thường gặp gồm:

- tạo table
- thêm row
- đọc data
- cập nhật data
- xóa data

## Ví dụ

```sql
SELECT id, name
FROM users
WHERE id = 10;
```

Câu query trên yêu cầu database trả về `id` và `name` từ table `users` với row có `id = 10`.

## Dễ nhầm với gì?

**SQL không phải tên của một database cụ thể.** PostgreSQL, MySQL và SQLite là các database system có hỗ trợ SQL.

**SQL không chỉ có SELECT.** SQL còn có command để định nghĩa structure và thay đổi data.

## Đọc tiếp

- [Table, Row và Column là gì?](table-row-column.md)
- [Index là gì?](index.md)

## Nguồn

- [PostgreSQL Documentation - The SQL Language](https://www.postgresql.org/docs/current/tutorial-sql.html)
- [PostgreSQL Documentation - SQL Language](https://www.postgresql.org/docs/current/sql.html)
