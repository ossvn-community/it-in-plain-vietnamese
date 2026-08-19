---
title: "SPI là gì?"
category: "embedded-iot"
core: false
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# SPI là gì?

SPI - Serial Peripheral Interface - là giao tiếp nối tiếp đồng bộ thường dùng giữa microcontroller và peripheral trên cùng board.

SPI thường có clock, đường dữ liệu theo hai chiều và tín hiệu chọn thiết bị. Cách đặt tên chân có thể khác nhau giữa tài liệu.

## Ví dụ

Một MCU có thể dùng SPI để đọc flash memory hoặc điều khiển display. MCU phát clock và chọn peripheral cần giao tiếp trước khi trao đổi dữ liệu.

## Dễ nhầm với gì?

SPI không có một chuẩn duy nhất quy định mọi chi tiết như một số protocol khác. Thiết bị cần thống nhất mode, tốc độ và cách đóng gói dữ liệu theo datasheet.

## Nguồn

- [Arduino Documentation - SPI](https://docs.arduino.cc/language-reference/en/functions/communication/SPI/)
