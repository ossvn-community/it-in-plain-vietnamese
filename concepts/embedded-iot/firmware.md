---
title: "Firmware là gì?"
category: "embedded-iot"
core: true
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# Firmware là gì?

Firmware là phần mềm chạy gần phần cứng của một thiết bị và điều khiển cách thiết bị hoạt động.

Trong hệ thống nhúng, firmware thường chạy trên microcontroller hoặc processor để đọc sensor, điều khiển actuator và thực hiện logic của sản phẩm.

## Tại sao cần nó?

Hardware tự nó không biết khi nào phải đọc sensor, bật motor hay gửi dữ liệu.

Firmware chứa logic để thiết bị thực hiện các hành vi đó.

## Ví dụ

Firmware của một thiết bị đo nhiệt độ có thể:

```text
Khởi động
  ↓
Đọc sensor
  ↓
Xử lý dữ liệu
  ↓
Hiển thị hoặc gửi kết quả
  ↓
Lặp lại
```

Firmware có thể được cập nhật nếu thiết bị và thiết kế hệ thống hỗ trợ việc đó.

## Dễ nhầm với gì?

Firmware vẫn là software.

Từ "firmware" thường nhấn mạnh software gắn chặt với hardware và vòng đời của thiết bị hơn application thông thường.

## Nguồn

- [NIST CSRC Glossary - Firmware](https://csrc.nist.gov/glossary/term/firmware)
- [NIST SP 800-193 - Platform Firmware Resiliency Guidelines](https://csrc.nist.gov/pubs/sp/800/193/final)
