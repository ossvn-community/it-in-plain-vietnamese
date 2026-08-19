---
title: "Web Storage là gì?"
category: "web"
core: false
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# Web Storage là gì?

Web Storage là API của trình duyệt cho phép website lưu dữ liệu dạng key-value trên máy người dùng.

Hai cơ chế thường gặp là `localStorage`, giữ dữ liệu qua nhiều phiên trình duyệt, và `sessionStorage`, gắn với một phiên/tab cụ thể.

## Ví dụ

Một website có thể lưu lựa chọn giao diện:
```js
localStorage.setItem("theme", "dark")
```
Lần sau mở trang, JavaScript có thể đọc giá trị này để khôi phục lựa chọn.

## Dễ nhầm với gì?

Web Storage khác Cookie. Dữ liệu Web Storage không tự động được gửi kèm mỗi HTTP request.

## Nguồn

- [MDN - Web Storage API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API)
