---
title: "RTOS là gì?"
category: "embedded-iot"
core: false
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# RTOS là gì?

RTOS - Real-Time Operating System - là hệ điều hành được thiết kế để các task có thể phản hồi trong giới hạn thời gian có thể dự đoán tốt hơn.

Trong embedded system, RTOS giúp tổ chức nhiều task, timer, interrupt và việc chia sẻ tài nguyên khi firmware trở nên phức tạp.

## Tại sao dùng RTOS?

Khi firmware có nhiều task cần chạy, RTOS có thể cung cấp scheduler và cơ chế để quản lý việc task nào được chạy vào thời điểm nào.

RTOS thường xuất hiện trong embedded systems, nhưng không phải mọi embedded system đều cần RTOS.

## Ví dụ

Một thiết bị có thể có các task:

```text
Task đọc sensor
Task xử lý dữ liệu
Task giao tiếp
Task cập nhật màn hình
```

RTOS scheduler quyết định task nào được chạy dựa trên policy và priority của hệ thống.

## Nguồn

- [FreeRTOS - RTOS Fundamentals](https://www.freertos.org/Documentation/01-FreeRTOS-quick-start/01-Beginners-guide/01-RTOS-fundamentals)
- [FreeRTOS - What is FreeRTOS?](https://www.freertos.org/Why-FreeRTOS/What-is-FreeRTOS)
