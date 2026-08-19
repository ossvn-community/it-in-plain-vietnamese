---
title: "UART là gì?"
category: "embedded-iot"
core: false
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# UART là gì?

UART - Universal Asynchronous Receiver/Transmitter - là cách giao tiếp nối tiếp phổ biến giữa hai thiết bị bằng đường truyền dữ liệu gửi và nhận.

Hai phía phải thống nhất các thông số như baud rate và định dạng frame để hiểu dữ liệu của nhau.

## Nó hoạt động thế nào?

Ở dạng đơn giản thường có hai đường dữ liệu:

```text
MCU A TX  ->  RX MCU B
MCU A RX  <-  TX MCU B
```

`TX` là transmit và `RX` là receive.

UART không cần đường clock riêng cho asynchronous communication, nên hai phía phải thống nhất timing trước.

## Ví dụ

UART thường được dùng để:

- Gửi log từ MCU tới máy tính qua một adapter phù hợp.
- Giao tiếp giữa MCU và module khác.
- Tạo command-line interface đơn giản cho thiết bị.

## Nguồn

- [Microchip - Getting Started with UART](https://onlinedocs.microchip.com/oxy/GUID-76576783-C495-405D-B106-CD04836134D0-en-US-2/GUID-5FA2C84E-8D5D-4532-A63B-8A8A9D5E3354.html)
- [Microchip - UART Peripheral](https://onlinedocs.microchip.com/oxy/GUID-420E6AAC-9141-47BF-A4C7-A6EA17246D0D-en-US-24/GUID-72640532-92DF-4282-A41F-217ECF028782.html)
