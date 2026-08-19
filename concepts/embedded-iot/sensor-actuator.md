---
title: "Sensor và Actuator là gì?"
category: "embedded-iot"
core: false
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# Sensor và Actuator là gì?

**Sensor** là thành phần đo hoặc nhận biết thông tin từ môi trường, như nhiệt độ, ánh sáng hoặc gia tốc.

**Actuator** là thành phần tạo ra tác động vật lý theo lệnh, như motor quay, relay đóng hoặc LED sáng. Hai loại này là cầu nối giữa phần mềm và thế giới vật lý.

## Tại sao cần chúng?

Embedded và IoT system thường cần hai chiều tương tác với thế giới vật lý:

```text
Thế giới vật lý
   ↓ Sensor
Embedded System
   ↓ Actuator
Thế giới vật lý
```

## Ví dụ

Trong hệ thống tưới cây:

- Sensor đo độ ẩm đất.
- MCU xử lý giá trị.
- Actuator điều khiển van nước.

Sensor và actuator không bắt buộc phải kết nối trực tiếp bằng GPIO; hệ thống có thể dùng các interface khác tùy thiết bị.

## Đọc tiếp

- [GPIO](gpio.md)
- [Internet of Things](internet-of-things.md)

## Nguồn

- [NIST - Cybersecurity for IoT Program FAQ](https://www.nist.gov/itl/applied-cybersecurity/nist-cybersecurity-iot-program/faqs)
- [NIST CSRC Glossary - Actuator](https://csrc.nist.gov/glossary/term/actuator)
- [NIST - Definitions for IEEE 1451 Sensors and Actuators](https://www.nist.gov/el/intelligent-systems-division-73500/definitions)
