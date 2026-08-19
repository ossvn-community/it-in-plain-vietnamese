---
title: "API là gì?"
category: "software-development"
core: true
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# API là gì?

API - Application Programming Interface - là cách một phần mềm cung cấp chức năng để phần mềm khác sử dụng theo một giao diện đã định nghĩa.

API giúp hai phần code làm việc với nhau mà bên sử dụng không cần biết toàn bộ chi tiết triển khai bên trong.

## Ví dụ

Một library có function:

```python
weather = get_weather("Hanoi")
```

Nếu `get_weather` là phần của public API, code khác chỉ cần tuân theo cách gọi đã được định nghĩa.

Một web service cũng có thể cung cấp API qua [HTTP](../web/http.md), nhưng **API không đồng nghĩa với HTTP API**. Library API và operating-system API cũng là API.

## Tại sao cần nó?

API tạo ranh giới rõ giữa phần cung cấp chức năng và phần sử dụng chức năng. Implementation bên trong có thể thay đổi miễn contract mà caller phụ thuộc vẫn được giữ phù hợp.

## Đọc tiếp

- [Function là gì?](function.md)
- [Abstraction là gì?](abstraction.md)
- [HTTP là gì?](../web/http.md)

## Nguồn

- [NIST CSRC - Application Programming Interface](https://csrc.nist.gov/glossary/term/Application_Programming_Interface)
