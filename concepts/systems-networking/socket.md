---
title: "Socket là gì?"
category: "systems-networking"
core: false
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# Socket là gì?

Socket là endpoint mà chương trình dùng để gửi hoặc nhận dữ liệu qua mạng.

Một socket thường gắn với protocol, địa chỉ và port để hệ điều hành biết dữ liệu thuộc về connection hoặc ứng dụng nào.

## Tại sao cần nó?

[IP Address](ip-address.md), [Port](port.md), TCP và UDP mô tả các phần của giao tiếp mạng.

Socket là interface mà application thường dùng để làm việc với các cơ chế đó qua hệ điều hành.

## Ví dụ

Một server TCP thường:

```text
create socket
    ↓
bind IP/port
    ↓
listen
    ↓
accept connection
```

Một ứng dụng UDP cũng dùng socket, nhưng cách gửi nhận dữ liệu khác TCP vì UDP là datagram-oriented.

## Dễ nhầm với gì?

**Socket không phải Port.** Port là một số dùng ở tầng transport. Socket là endpoint/interface mà process dùng để giao tiếp.

**Socket không đồng nghĩa với TCP.** Socket có thể được dùng với nhiều protocol và kiểu giao tiếp khác nhau.

## Đọc tiếp

- [Port là gì?](port.md)
- [TCP và UDP là gì?](tcp-udp.md)

## Nguồn

- [POSIX.1-2024 - Socket definition](https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap03.html)
- [Microsoft Learn - socket function](https://learn.microsoft.com/en-us/windows/win32/api/winsock2/nf-winsock2-socket)
