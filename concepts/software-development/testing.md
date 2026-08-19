---
title: "Testing là gì?"
category: "software-development"
core: false
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# Testing là gì?

Testing - kiểm thử - là quá trình kiểm tra phần mềm có hoạt động như mong đợi trong các trường hợp quan trọng hay không.

Test có thể được chạy thủ công hoặc tự động, từ một function nhỏ tới toàn bộ flow của hệ thống.

## Ví dụ

Với function:

```python
def add(a, b):
    return a + b
```

Một test đơn giản có thể kiểm tra:

```python
assert add(2, 3) == 5
```

Test không chứng minh phần mềm không còn bug. Nó kiểm tra những case mà bạn đã thiết kế để chạy.

## Đọc tiếp

- [Function là gì?](function.md)
- [Debugging là gì?](debugging.md)

## Nguồn

- [Python Documentation - unittest, Unit Testing Framework](https://docs.python.org/3/library/unittest.html)
