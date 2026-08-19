---
title: "Internet of Things (IoT) là gì?"
category: "embedded-iot"
core: true
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# Internet of Things (IoT) là gì?

Internet of Things - Internet vạn vật, thường viết tắt là **IoT** - là nhóm hệ thống trong đó thiết bị vật lý có khả năng thu thập dữ liệu, trao đổi qua mạng và phối hợp với phần mềm khác.

Một hệ thống IoT thường kết hợp thiết bị, kết nối mạng, backend và ứng dụng người dùng.

## Một IoT system có thể gồm gì?

```text
Sensor / Actuator
       ↓
    IoT device
       ↓
     Network
       ↓
Backend / Cloud / App
```

Không phải hệ thống nào cũng có đúng flow này, nhưng nó cho thấy IoT thường liên quan cả physical device, computing và communication.

## Ví dụ

Một cảm biến nhiệt độ có network interface có thể gửi dữ liệu tới backend để người dùng xem trên mobile app.

Thiết bị có thể dùng MQTT, [HTTP](../web/http.md) hoặc protocol khác tùy thiết kế.

## Đọc tiếp

- [Sensor và Actuator](sensor-actuator.md)
- [MQTT](mqtt.md)
- [IP Address](../systems-networking/ip-address.md) - khi hệ thống dùng mạng IP.

## Nguồn

- [NIST - Cybersecurity for IoT Program FAQ](https://www.nist.gov/itl/applied-cybersecurity/nist-cybersecurity-iot-program/faqs)
- [NIST CSRC Glossary - IoT Device](https://csrc.nist.gov/glossary/term/iot_device)
- [NIST SP 800-183 - Networks of 'Things'](https://www.nist.gov/publications/networks-things)
