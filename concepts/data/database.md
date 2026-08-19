---
title: "Database là gì?"
category: "data"
core: true
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# Database là gì?

Database - cơ sở dữ liệu - là hệ thống tổ chức dữ liệu để có thể lưu lâu dài, tìm lại, cập nhật và quản lý có cấu trúc.

Ứng dụng thường dùng database khi dữ liệu cần tồn tại qua nhiều lần chạy và được truy cập theo nhiều cách.

## Tại sao cần nó?

Database cung cấp cách có cấu trúc để lưu data lâu dài, truy xuất và cập nhật khi cần.

Database management system - DBMS - là phần mềm quản lý database.

## Ví dụ

Một ứng dụng bán hàng có thể lưu:

```text
users
products
orders
payments
```

Trong relational database, các nhóm data này thường được tổ chức thành table. Nhưng cũng có các mô hình database khác.

## Dễ nhầm với gì?

**Database không đồng nghĩa với SQL.** SQL là language phổ biến để làm việc với relational database. Không phải mọi database đều dùng SQL theo cùng cách.

**Database không đồng nghĩa với table.** Một relational database thường chứa nhiều table và object khác.

## Đọc tiếp

- [Relational Database là gì?](relational-database.md)
- [SQL là gì?](sql.md)
- [Table, Row và Column là gì?](table-row-column.md)

## Nguồn

- [NIST CSRC - Database](https://csrc.nist.gov/glossary/term/Database)
- [PostgreSQL Documentation - Concepts](https://www.postgresql.org/docs/current/tutorial-concepts.html)
