---
title: "Variable là gì?"
category: "software-development"
core: true
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# Variable là gì?

Variable - biến - là một tên mà chương trình dùng để tham chiếu tới một giá trị hoặc dữ liệu có thể được sử dụng trong quá trình chạy.

Variable giúp code làm việc với dữ liệu bằng tên có ý nghĩa thay vì lặp lại giá trị trực tiếp ở mọi nơi.

## Ví dụ

Python:

```python
age = 20
age = age + 1
print(age)
```

Tên `age` ban đầu được bind với giá trị `20`, sau đó được bind lại với giá trị `21`.

## Tại sao cần nó?

Variable giúp chương trình giữ và sử dụng dữ liệu bằng tên có ý nghĩa:

```python
price = 100
quantity = 3
total = price * quantity
```

## Dễ nhầm với gì?

**Variable không phải lúc nào cũng là một "ô nhớ" cố định.** Mô hình chính xác khác nhau giữa các language. Với Python, name được bind tới object.

## Đọc tiếp

- [Data Type là gì?](data-type.md)
- [Function là gì?](function.md)

## Nguồn

- [Python Documentation - Execution Model: Naming and Binding](https://docs.python.org/3/reference/executionmodel.html)
