---
title: "Client và Server là gì?"
category: "web"
core: true
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# Client và Server là gì?

Client và Server là hai vai trò thường gặp khi các chương trình giao tiếp qua mạng.

**Client** gửi request hoặc bắt đầu tương tác; **server** cung cấp dữ liệu hoặc dịch vụ để phản hồi. Một chương trình có thể đóng vai trò khác nhau trong các tình huống khác nhau.

## Nó hoạt động thế nào?

Với HTTP:

```text
Client  -- request -->  Server
Client  <-- response -- Server
```

Vai trò client/server mô tả hai phía của một tương tác. Một chương trình có thể là server trong kết nối này nhưng lại là client khi nó gọi một service khác.

## Ví dụ

Khi bạn mở một trang:

1. [Browser](browser.md) gửi HTTP request.
2. Web server nhận request.
3. Server trả HTTP response chứa HTML hoặc dữ liệu khác.
4. Browser xử lý response.

## Tại sao cần nó?

Khái niệm này là nền cho việc hiểu [HTTP](http.md), API, frontend/backend và cách các service giao tiếp.

## Thử ngay

```bash
curl -i https://example.com
```

Trong ví dụ này, `curl` đóng vai trò client; server của `example.com` trả response.

## Dễ nhầm với gì?

**Client và server là vai trò, không nhất thiết là hai loại máy cố định.**

## Đọc tiếp

- [HTTP là gì?](http.md)
- [Browser là gì?](browser.md)

## Nguồn

- [RFC 9110 - Connections, Clients, and Servers](https://www.rfc-editor.org/rfc/rfc9110#section-3.3)
- [MDN - Client-server overview](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/First_steps/Client-Server_overview)
