---
title: "Function là gì?"
category: "software-development"
core: true
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# Function là gì?

Function - hàm - là một khối code được đặt tên để thực hiện một công việc và có thể được gọi lại nhiều lần.

Function giúp chia chương trình thành các phần nhỏ hơn, tái sử dụng logic và làm code dễ đọc hơn.

## Ví dụ

Python:

```python
def add(a, b):
    return a + b

result = add(2, 3)
```

`add` được định nghĩa một lần và có thể gọi nhiều lần với input khác nhau.

## Tại sao cần nó?

Function giúp:

- chia chương trình thành các phần nhỏ;
- đặt tên cho một công việc;
- tái sử dụng logic;
- tạo abstraction để caller không phải biết mọi chi tiết bên trong.

## Dễ nhầm với gì?

**Định nghĩa function chưa có nghĩa là body đã chạy.** Trong Python, body chạy khi function được gọi.

## Đọc tiếp

- [Abstraction là gì?](abstraction.md)
- [API là gì?](api.md)

## Nguồn

- [Python Documentation - Function Definitions](https://docs.python.org/3/reference/compound_stmts.html#function-definitions)
- [MIT OpenCourseWare - Decomposition, Abstraction, Functions](https://ocw.mit.edu/courses/6-100l-introduction-to-cs-and-programming-using-python-fall-2022/pages/lecture-7-decomposition-abstraction-functions/)
