---
title: "CAN là gì?"
category: "embedded-iot"
core: false
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# CAN là gì?

CAN - Controller Area Network - là bus truyền thông được thiết kế để nhiều node trao đổi message tin cậy trong môi trường có nhiễu, đặc biệt phổ biến trong ô tô và hệ thống công nghiệp.

CAN dùng cơ chế arbitration để nhiều node chia sẻ bus mà không cần một master duy nhất điều khiển mọi lần truyền.

## Ví dụ

Trong xe, các ECU có thể gửi message về tốc độ, trạng thái nút bấm hoặc dữ liệu cảm biến trên cùng CAN bus. Node quan tâm sẽ nhận message theo identifier.

## Dễ nhầm với gì?

CAN mô tả lớp truyền thông ở mức bus/frame. Các protocol cao hơn như CANopen, J1939 hoặc một số giao thức automotive có thể xây phía trên CAN.

## Nguồn

- [Zephyr Documentation - CAN Controller](https://docs.zephyrproject.org/latest/hardware/peripherals/can/controller.html)
