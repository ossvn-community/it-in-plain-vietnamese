---
title: "HTTP là gì?"
category: "web"
core: true
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# HTTP là gì?

HTTP - Hypertext Transfer Protocol - là protocol dùng để client và server trao đổi request và response trên Web.

Browser dùng HTTP để yêu cầu HTML, ảnh hoặc dữ liệu API; server trả về status, header và nội dung phù hợp.

## Nó hoạt động thế nào?

Một [client](client-server.md) gửi request tới server. Server xử lý request rồi gửi response trở lại.

```text
Client
  │
  │  GET /docs
  ▼
Server
  │
  │  200 OK + content
  ▼
Client
```

Request có method như `GET`, `POST`; response có status code như `200`, `404`, `500`.

Tài nguyên đích thường được xác định bằng [URL](url.md).

## Tại sao cần nó?

Khi browser tải trang, gọi API hoặc gửi form, HTTP thường là protocol mô tả request muốn làm gì và response trả lại kết quả gì.

## Thử ngay

```bash
curl -I https://example.com
```

Lệnh này gửi request và in response headers.

## Dễ nhầm với gì?

**HTTP không phải Internet.** HTTP chạy trên hạ tầng mạng và transport bên dưới nó.

**HTTPS không phải một protocol Web hoàn toàn khác.** HTTPS dùng HTTP qua một kết nối được bảo vệ bằng TLS.

## Đọc tiếp

- [Client và Server là gì?](client-server.md)
- [URL là gì?](url.md)
- [Browser là gì?](browser.md)

## Nguồn

- [RFC 9110 - HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110)
- [MDN - HTTP overview](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview)
