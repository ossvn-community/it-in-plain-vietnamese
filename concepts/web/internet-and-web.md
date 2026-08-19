---
title: "Internet và Web là gì?"
category: "web"
core: true
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# Internet và Web là gì?

Internet là hạ tầng mạng toàn cầu kết nối nhiều mạng và thiết bị với nhau. Web là một dịch vụ chạy trên Internet, sử dụng các công nghệ như URL, HTTP và browser để truy cập tài liệu và ứng dụng.

Vì vậy Internet và Web liên quan chặt chẽ nhưng không phải cùng một thứ.

## Tại sao cần phân biệt?

Web dùng Internet, nhưng Internet còn phục vụ nhiều thứ khác ngoài Web.

Hiểu sự khác nhau này giúp bạn không đồng nhất website, browser hay HTTP với toàn bộ Internet.

## Một lần mở website diễn ra thế nào?

Ở mức đơn giản:

```text
URL
 ↓
DNS tìm địa chỉ server
 ↓
Client kết nối tới server qua Internet
 ↓
HTTP request / response
 ↓
Browser xử lý tài nguyên nhận được
```

Các bước này liên quan trực tiếp tới [URL](url.md), [DNS](dns.md), [Client và Server](client-server.md) và [HTTP](http.md).

## Ví dụ

Khi mở `https://example.com/`, browser dùng Internet để liên lạc với server của website. Web là lớp tài nguyên và giao thức mà bạn đang sử dụng trên hạ tầng đó.

## Dễ nhầm với gì?

**Internet không phải Web.** Web là một hệ thống được xây trên Internet.

## Đọc tiếp

- [URL là gì?](url.md)
- [DNS là gì?](dns.md)
- [Client và Server là gì?](client-server.md)
- [HTTP là gì?](http.md)

## Nguồn

- [MDN - How does the Internet work?](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/How_does_the_Internet_work)
- [MDN - The web standards model](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/The_web_standards_model)
