---
title: "Port là gì?"
category: "systems-networking"
core: true
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# Port là gì?

Port là một số dùng cùng địa chỉ IP để phân biệt các dịch vụ hoặc connection trên cùng một máy.

Nhờ port, một server có thể đồng thời chạy nhiều dịch vụ mạng khác nhau mà vẫn dùng chung một địa chỉ IP.

## Tại sao cần nó?

Một máy có thể chạy nhiều dịch vụ mạng cùng lúc.

[IP Address](ip-address.md) giúp packet tới đúng host. Port giúp dữ liệu được chuyển tiếp tới đúng endpoint của dịch vụ trên host đó.

```text
IP Address + Transport Protocol + Port
```

Ba thông tin này thường xuất hiện cùng nhau khi ứng dụng giao tiếp qua mạng.

## Ví dụ

HTTPS thường dùng service name `https` với port `443` được đăng ký cho TCP và UDP trong registry của IANA.

Điều đó không có nghĩa cứ thấy traffic ở port `443` thì chắc chắn đó là HTTPS. Port number chỉ là một phần thông tin của giao tiếp mạng.

## Dễ nhầm với gì?

**Port không phải cổng vật lý.** Đây là một số logic trong giao tiếp mạng.

**Port không tự xác định protocol.** Cùng một số port có thể có đăng ký cho nhiều transport protocol khác nhau.

## Đọc tiếp

- [TCP và UDP là gì?](tcp-udp.md)
- [Socket là gì?](socket.md)

## Nguồn

- [IANA - Service Name and Transport Protocol Port Number Registry](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml)
- [RFC 6335 - Internet Assigned Numbers Authority Procedures for Service Names and Transport Protocol Port Numbers](https://www.rfc-editor.org/rfc/rfc6335.html)
