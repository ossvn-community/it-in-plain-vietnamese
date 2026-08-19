---
title: "Cache là gì?"
category: "data"
core: false
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# Cache là gì?

Cache là nơi giữ tạm dữ liệu đã có hoặc kết quả đã tính để lần truy cập sau có thể nhanh hơn.

Cache đánh đổi thêm không gian lưu trữ và độ phức tạp để giảm thời gian chờ hoặc giảm tải cho nguồn dữ liệu gốc.

## Ví dụ

Một API phải đọc cùng thông tin sản phẩm từ database hàng nghìn lần. Hệ thống có thể cache kết quả trong một khoảng thời gian để nhiều request đọc từ cache thay vì truy vấn database mỗi lần.

## Dễ nhầm với gì?

Cache không phải nguồn dữ liệu chính. Dữ liệu trong cache có thể cũ hoặc bị xóa, nên hệ thống cần quy tắc về thời hạn và cách làm mới.

## Nguồn

- [MDN - HTTP caching](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Caching)
