---
title: "CORS là gì?"
category: "web"
core: false
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# CORS là gì?

CORS - Cross-Origin Resource Sharing - là cơ chế HTTP cho phép server nói với trình duyệt origin nào được phép đọc response từ một request cross-origin.

Nó là một phần của mô hình bảo mật trên trình duyệt, đặc biệt khi JavaScript ở một website gọi tài nguyên từ domain khác.

## Ví dụ

Frontend chạy ở `https://app.example` gọi API ở `https://api.example`. Server API có thể gửi các CORS header phù hợp để trình duyệt cho phép JavaScript của frontend đọc response.

## Dễ nhầm với gì?

CORS không phải cơ chế xác thực người dùng và cũng không ngăn mọi loại request tới server. Nó chủ yếu điều khiển việc trình duyệt cho script ở origin khác truy cập response.

## Nguồn

- [MDN - Cross-Origin Resource Sharing](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS)
