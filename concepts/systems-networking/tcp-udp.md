---
title: "TCP và UDP là gì?"
category: "systems-networking"
core: true
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# TCP và UDP là gì?

TCP và UDP là hai transport protocol phổ biến chạy trên IP để ứng dụng trao đổi dữ liệu qua mạng.

TCP ưu tiên truyền dữ liệu có thứ tự và đáng tin cậy hơn; UDP đơn giản hơn, không tự cung cấp các đảm bảo giống TCP và phù hợp với những nhu cầu khác.

## Tại sao cần phân biệt?

Ứng dụng có yêu cầu khác nhau về reliability, ordering và cách truyền dữ liệu.

TCP tự xử lý nhiều việc như phát hiện mất dữ liệu và retransmission. UDP để nhiều quyết định hơn cho application hoặc protocol ở tầng trên.

Không nên hiểu đơn giản rằng "TCP chậm, UDP nhanh". Trade-off thực tế phụ thuộc vào yêu cầu của ứng dụng và protocol được xây phía trên.

## Nó liên quan tới IP và Port thế nào?

Ở mức đơn giản:

```text
Application data
      ↓
TCP hoặc UDP + Port
      ↓
IP + IP Address
      ↓
Network
```

TCP và UDP đều dùng port number để phân biệt endpoint giao tiếp.

## Ví dụ

Một ứng dụng cần byte stream đáng tin cậy có thể dùng TCP.

Một protocol muốn tự quản lý cách xử lý datagram có thể dùng UDP.

## Đọc tiếp

- [IP Address là gì?](ip-address.md)
- [Port là gì?](port.md)
- [Socket là gì?](socket.md)

## Nguồn

- [RFC 9293 - Transmission Control Protocol](https://www.rfc-editor.org/rfc/rfc9293.html)
- [RFC 768 - User Datagram Protocol](https://www.rfc-editor.org/rfc/rfc768.html)
