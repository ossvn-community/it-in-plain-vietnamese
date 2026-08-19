---
title: "I2C là gì?"
category: "embedded-iot"
core: false
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# I2C là gì?

I2C - Inter-Integrated Circuit - là giao tiếp nối tiếp thường dùng để các chip trên cùng board trao đổi dữ liệu qua hai đường tín hiệu chính: SDA cho dữ liệu và SCL cho clock.

Nhiều thiết bị có thể dùng chung bus và được phân biệt bằng address.

## Ví dụ

Một microcontroller có thể đọc cảm biến nhiệt độ qua I2C. MCU tạo clock trên SCL, gửi address của cảm biến và trao đổi byte dữ liệu qua SDA.

## Dễ nhầm với gì?

I2C thường phù hợp cho giao tiếp khoảng cách ngắn trên board. Nó khác UART ở cách tổ chức bus và khác SPI ở số dây, tốc độ và cơ chế chọn thiết bị.

## Nguồn

- [NXP - UM10204 I2C-bus specification and user manual](https://www.nxp.com/docs/en/user-guide/UM10204.pdf)
