---
title: "Logging là gì?"
category: "cloud-devops"
core: false
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# Logging là gì?

Logging là việc chương trình ghi lại các event hoặc thông tin quan trọng trong quá trình chạy.

Log giúp developer và operator hiểu chuyện gì đã xảy ra, đặc biệt khi cần debug lỗi hoặc điều tra sự cố sau đó.

## Ví dụ

Một API có thể ghi:
```text
2026-08-19 INFO request_id=abc user=42 action=checkout
2026-08-19 ERROR request_id=abc payment_timeout
```
Nhờ cùng `request_id`, người vận hành có thể nối các event liên quan.

## Dễ nhầm với gì?

Log không nên chứa secret hoặc dữ liệu nhạy cảm chỉ vì “để debug”. Cần chọn nội dung, mức log và thời gian lưu phù hợp.

## Nguồn

- [OpenTelemetry - Logs](https://opentelemetry.io/docs/concepts/signals/logs/)
