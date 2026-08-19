---
title: "URL là gì?"
category: "web"
core: true
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# URL là gì?

URL - Uniform Resource Locator - là địa chỉ mô tả nơi một resource có thể được truy cập và cách truy cập nó.

Trên Web, URL thường gồm scheme như `https`, host, path và có thể thêm query hoặc fragment.

## Nó gồm những phần nào?

Ví dụ:

```text
https://example.com/docs/page?lang=vi#intro
│      │           │         │      │
scheme host        path      query  fragment
```

- `https` - scheme, cho biết cách truy cập.
- `example.com` - host.
- `/docs/page` - path tới tài nguyên trong namespace của host.
- `?lang=vi` - query, dữ liệu bổ sung cho request.
- `#intro` - fragment, chỉ một phần trong tài nguyên.

Không phải URL nào cũng có đầy đủ mọi phần.

## Tại sao cần nó?

[HTTP](http.md) request cần xác định resource đích. URL là cách phổ biến để browser và ứng dụng biểu diễn địa chỉ đó.

Host trong URL thường cần được [DNS](dns.md) phân giải trước khi client có thể kết nối tới server.

## Thử ngay

Nhìn URL của trang hiện tại và thử tách `scheme`, `host`, `path`, `query`, `fragment` nếu chúng tồn tại.

## Dễ nhầm với gì?

**Domain name chỉ là một phần có thể xuất hiện trong URL.** `example.com` không phải toàn bộ `https://example.com/docs`.

## Đọc tiếp

- [DNS là gì?](dns.md)
- [HTTP là gì?](http.md)

## Nguồn

- [WHATWG - URL Standard](https://url.spec.whatwg.org/)
- [RFC 3986 - Uniform Resource Identifier: Generic Syntax](https://www.rfc-editor.org/rfc/rfc3986)
