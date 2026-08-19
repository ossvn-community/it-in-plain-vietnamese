---
title: "MQTT là gì?"
category: "embedded-iot"
core: false
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# MQTT là gì?

MQTT là protocol nhắn tin nhẹ theo mô hình publish/subscribe, thường được dùng trong IoT và các hệ thống có thiết bị kết nối qua mạng.

Thay vì các thiết bị gửi trực tiếp cho nhau, chúng thường publish message tới broker và subscribe các topic mà mình quan tâm.

## Publish/Subscribe là gì?

Thay vì client gửi message trực tiếp cho từng client khác, MQTT tổ chức message theo topic thông qua MQTT server/broker.

```text
Publisher
   ↓ publish topic
MQTT Server
   ↓
Subscriber
```

Subscriber đăng ký các topic mà nó quan tâm.

## MQTT có phải IoT không?

Không.

[Internet of Things](internet-of-things.md) là khái niệm về hệ thống/kết nối thiết bị. MQTT chỉ là một protocol có thể được chọn làm một phần của hệ thống đó.

Một IoT system cũng có thể dùng HTTP hoặc các protocol khác.

## Nguồn

- [OASIS Standard - MQTT Version 5.0](https://www.oasis-open.org/standard/mqtt-v5-0-os/)
- [OASIS - MQTT Version 5.0 Specification](https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html)
