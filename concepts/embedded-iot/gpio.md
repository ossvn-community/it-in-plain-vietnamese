---
title: "GPIO là gì?"
category: "embedded-iot"
core: true
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# GPIO là gì?

GPIO - General-Purpose Input/Output - là các chân tín hiệu trên microcontroller hoặc processor có thể được cấu hình để đọc tín hiệu vào hoặc điều khiển tín hiệu ra.

GPIO là một trong những cách đơn giản nhất để phần mềm tương tác trực tiếp với phần cứng bên ngoài.

## Input và Output

Ở mức beginner:

- **Input**: đọc trạng thái digital từ bên ngoài, ví dụ button.
- **Output**: đặt trạng thái digital để điều khiển thứ khác, ví dụ LED.

## Ví dụ

```text
Button -> GPIO input -> MCU -> GPIO output -> LED
```

Khi button thay đổi trạng thái, firmware có thể đọc GPIO input rồi thay đổi GPIO output.

## Dễ nhầm với gì?

GPIO không thay thế các communication interface như UART, I2C hoặc SPI.

Một số pin trên MCU có thể có nhiều chức năng, nhưng cách cấu hình cụ thể phụ thuộc vào chip.

## Đọc tiếp

- [Sensor và Actuator](sensor-actuator.md)
- [UART](uart.md)

## Nguồn

- [Linux Kernel Documentation - What is a GPIO?](https://docs.kernel.org/6.5/driver-api/gpio/intro.html)
- [Microchip - Getting Started with GPIO](https://onlinedocs.microchip.com/oxy/GUID-76576783-C495-405D-B106-CD04836134D0-en-US-2/GUID-7450F688-F426-4E9A-8AAD-D393CB10ED8E.html)
