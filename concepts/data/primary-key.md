---
title: "Primary Key là gì?"
category: "data"
core: false
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# Primary Key là gì?

Primary Key - khóa chính - là column hoặc nhóm column dùng để xác định duy nhất mỗi row trong một relational table.

Nhờ primary key, database và application có một cách rõ ràng để nói tới đúng một bản ghi.

## Tại sao cần nó?

Application thường cần cách ổn định để biết chính xác đang nói tới row nào.

Primary key tạo ra một identifier rõ ràng và cũng là target mặc định thường được dùng khi table khác tạo foreign key reference tới table này.

## Ví dụ

```sql
CREATE TABLE users (
    id integer PRIMARY KEY,
    name text NOT NULL
);
```

Trong table này, hai row không thể có cùng `id`, và `id` không được để null.

## Dễ nhầm với gì?

**Primary Key không đơn giản là "column có index".** Trong PostgreSQL, tạo primary key sẽ tự tạo unique index phù hợp, nhưng primary key còn mang ý nghĩa constraint và identifier của row.

**Một table chỉ có một primary key**, dù primary key đó có thể gồm nhiều column.

## Đọc tiếp

- [Table, Row và Column là gì?](table-row-column.md)
- [Index là gì?](index.md)

## Nguồn

- [PostgreSQL Documentation - Constraints](https://www.postgresql.org/docs/current/ddl-constraints.html)
