---
title: "Index là gì?"
category: "data"
core: true
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# Index là gì?

Database Index là một cấu trúc bổ sung giúp database tìm một số dữ liệu nhanh hơn mà không phải luôn đọc toàn bộ table.

Đổi lại, index cần thêm storage và có thể làm việc ghi dữ liệu tốn thêm công sức vì index cũng phải được cập nhật.

## Tại sao cần nó?

Index hữu ích khi query thường xuyên cần tìm dữ liệu theo column hoặc expression mà index có thể hỗ trợ.

Lợi ích cụ thể phụ thuộc vào query và workload của database.

## Ví dụ

Giả sử application thường tìm user theo email:

```sql
SELECT id, name
FROM users
WHERE email = 'an@example.com';
```

Bạn có thể tạo index:

```sql
CREATE INDEX users_email_idx ON users (email);
```

Database query planner có thể dùng index đó khi thấy phù hợp.

## Trade-off cơ bản

Index không phải "càng nhiều càng tốt".

Mỗi index cần storage và có thể tạo thêm công việc khi data được insert, update hoặc delete. Vì vậy lợi ích của index phụ thuộc vào cách database được đọc và ghi.

## Đọc tiếp

- [Table, Row và Column là gì?](table-row-column.md)
- [Primary Key là gì?](primary-key.md)

## Nguồn

- [PostgreSQL Documentation - Indexes](https://www.postgresql.org/docs/current/indexes.html)
