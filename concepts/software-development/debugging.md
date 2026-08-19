---
title: "Debugging là gì?"
category: "software-development"
core: false
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# Debugging là gì?

Debugging là quá trình tìm nguyên nhân và sửa lỗi trong chương trình.

Thay vì chỉ sửa thử ngẫu nhiên, debugging thường gồm tái hiện lỗi, quan sát trạng thái, thu hẹp nguyên nhân rồi kiểm tra lại bản sửa.

## Ví dụ

Đoạn code này lỗi khi `b = 0`:

```python
def divide(a, b):
    return a / b
```

Khi debug, bạn có thể kiểm tra giá trị của `a`, `b` và call stack tại vị trí lỗi thay vì chỉ đoán nguyên nhân.

## Thử ngay

Python có built-in debugger:

```python
breakpoint()
```

Khi chương trình dừng tại đây, bạn có thể inspect variable và chạy tiếp từng bước.

## Nguồn

- [Python Documentation - pdb, The Python Debugger](https://docs.python.org/3/library/pdb.html)
