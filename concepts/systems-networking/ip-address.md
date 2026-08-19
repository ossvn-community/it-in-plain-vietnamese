---
title: "IP Address là gì?"
category: "systems-networking"
core: true
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# IP Address là gì?

IP Address - địa chỉ IP - là địa chỉ dùng để xác định một interface trên mạng IP để dữ liệu có thể được gửi tới đúng nơi.

IPv4 thường có dạng như `192.168.1.10`, còn IPv6 dùng định dạng dài hơn như `2001:db8::1`.

## Tại sao cần nó?

Khi hai thiết bị giao tiếp qua mạng IP, packet cần biết nó đi từ đâu và cần tới đâu.

IP Address giải quyết phần định danh ở mức mạng. Sau đó các protocol như TCP hoặc UDP dùng thêm [Port](port.md) để phân biệt endpoint của ứng dụng.

## Ví dụ

Hai dạng địa chỉ thường gặp:

```text
IPv4: 192.0.2.10
IPv6: 2001:db8::10
```

Địa chỉ IP không nhất thiết là địa chỉ cố định hoặc duy nhất trên toàn Internet trong mọi trường hợp. Ví dụ, mạng riêng có thể dùng private IP và đi ra Internet qua cơ chế khác.

## Dễ nhầm với gì?

**IP Address không phải domain name.** `example.com` là tên dễ đọc cho con người. DNS có thể giúp tìm địa chỉ IP tương ứng với tên đó.

**IP Address không phải Port.** IP giúp xác định đích ở mức mạng; port giúp phân biệt dịch vụ hoặc endpoint ở tầng transport.

## Đọc tiếp

- [Port là gì?](port.md)
- [TCP và UDP là gì?](tcp-udp.md)

## Nguồn

- [RFC 8200 - Internet Protocol, Version 6 Specification](https://www.rfc-editor.org/rfc/rfc8200.html)
- [RFC 791 - Internet Protocol](https://www.rfc-editor.org/rfc/rfc791.html)
