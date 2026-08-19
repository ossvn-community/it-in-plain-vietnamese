---
title: "Observability là gì?"
category: "cloud-devops"
core: false
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# Observability là gì?

Observability - khả năng quan sát - là mức độ bạn có thể hiểu trạng thái bên trong của hệ thống dựa trên dữ liệu mà hệ thống phát ra.

Logs, metrics và traces là các tín hiệu thường dùng để điều tra vì sao một hệ thống chậm, lỗi hoặc hoạt động khác kỳ vọng.

## Ví dụ

Một API có latency tăng. Metrics cho thấy request chậm, trace chỉ ra thời gian bị kẹt ở database call, còn log cung cấp chi tiết lỗi tại thời điểm đó. Kết hợp các tín hiệu giúp tìm nguyên nhân nhanh hơn.

## Dễ nhầm với gì?

Observability không chỉ là “có dashboard”. Nó còn phụ thuộc việc hệ thống phát ra dữ liệu đủ hữu ích để đặt câu hỏi mới khi sự cố xảy ra.

## Nguồn

- [OpenTelemetry - Observability Primer](https://opentelemetry.io/docs/concepts/observability-primer/)
