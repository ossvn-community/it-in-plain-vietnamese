---
title: "Transaction là gì?"
category: "data"
core: false
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# Transaction là gì?

Transaction là một nhóm thao tác với database được xử lý như một đơn vị công việc.

Mục tiêu là giúp nhiều thay đổi liên quan được hoàn tất cùng nhau hoặc được hủy khi có lỗi, thay vì để database ở trạng thái dở dang.

## Ví dụ

Chuyển tiền giữa hai tài khoản thường gồm ít nhất hai thay đổi: trừ tiền ở tài khoản A và cộng tiền vào tài khoản B. Đặt chúng trong một transaction giúp tránh trường hợp chỉ một nửa thao tác được ghi nhận.

## Dễ nhầm với gì?

Transaction không có nghĩa mọi thao tác luôn thành công. Nó cung cấp cơ chế để commit khi hợp lệ hoặc rollback khi cần.

## Nguồn

- [PostgreSQL Documentation - Transactions](https://www.postgresql.org/docs/current/tutorial-transactions.html)
