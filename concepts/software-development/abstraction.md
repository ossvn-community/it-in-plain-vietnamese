---
title: "Abstraction là gì?"
category: "software-development"
core: false
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# Abstraction là gì?

Abstraction - trừu tượng hóa - là cách chỉ giữ lại những phần cần thiết để sử dụng hoặc hiểu một thứ, đồng thời ẩn bớt các chi tiết phức tạp bên trong.

Nhờ abstraction, bạn có thể làm việc với một hệ thống mà không cần hiểu toàn bộ cách nó được triển khai.

## Ví dụ đời thường

Một cách hình dung đơn giản là việc lái ô tô.

Bạn dùng vô lăng, chân ga và chân phanh để điều khiển xe mà không cần biết chính xác động cơ, hộp số và các hệ thống bên trong đang phối hợp thế nào ở từng thời điểm.

Các bộ phận điều khiển cung cấp phần bạn cần để sử dụng chiếc xe, còn nhiều chi tiết kỹ thuật được ẩn phía sau.

## Ví dụ trong lập trình

Khi gọi một function:

```python
result = max(3, 7)
```

Bạn cần biết `max` nhận các giá trị đầu vào và trả về giá trị lớn nhất. Bạn không cần đọc toàn bộ code bên trong function trước khi sử dụng nó.

Đó là một abstraction: cách sử dụng được tách khỏi chi tiết triển khai.

## Tại sao cần nó?

Abstraction xuất hiện ở nhiều nơi trong IT:

- Function che giấu các bước xử lý bên trong.
- API đưa ra cách để phần mềm khác sử dụng một chức năng.
- File cho phép chương trình làm việc với dữ liệu mà không cần trực tiếp điều khiển thiết bị lưu trữ.

Abstraction giúp chia hệ thống phức tạp thành các lớp dễ làm việc hơn.

## Đọc tiếp

- [Function là gì?](function.md)
- [API là gì?](api.md)

## Nguồn

- [MIT OpenCourseWare - Decomposition, Abstraction, Functions](https://ocw.mit.edu/courses/6-100l-introduction-to-cs-and-programming-using-python-fall-2022/pages/lecture-7-decomposition-abstraction-functions/)
