---
title: "DOM là gì?"
category: "web"
core: false
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# DOM là gì?

DOM - Document Object Model - là cách trình duyệt biểu diễn tài liệu HTML thành một cấu trúc object để code có thể đọc và thay đổi.

Nhờ DOM, JavaScript có thể tìm một phần tử trên trang, đổi nội dung, thêm phần tử mới hoặc phản hồi sự kiện.

## Ví dụ

Với HTML có một nút `id="save"`, JavaScript có thể dùng `document.getElementById("save")` để lấy object đại diện cho nút đó và gắn xử lý khi người dùng click.

## Dễ nhầm với gì?

DOM không phải chính file HTML. HTML là nội dung nguồn; DOM là mô hình mà trình duyệt tạo ra và cung cấp qua API.

## Nguồn

- [MDN - Document Object Model](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model)
