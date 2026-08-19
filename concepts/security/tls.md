---
title: "TLS là gì?"
category: "security"
core: false
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# TLS là gì?

TLS - Transport Layer Security - là protocol giúp bảo vệ dữ liệu khi hai bên giao tiếp qua mạng.

TLS cung cấp cơ chế mã hóa dữ liệu trên đường truyền, xác thực danh tính bằng certificate trong các trường hợp phổ biến và phát hiện dữ liệu bị sửa đổi.

## Ví dụ

Khi bạn mở một website bằng `https://`, trình duyệt thường thiết lập kết nối TLS với server trước khi trao đổi HTTP. Nhờ đó nội dung đăng nhập hoặc dữ liệu khác không được gửi dưới dạng dễ đọc trực tiếp trên mạng.

## Dễ nhầm với gì?

TLS không tự bảo vệ mọi thứ trên website. Nó bảo vệ kênh truyền; lỗ hổng trong application, mật khẩu yếu hoặc server bị xâm nhập vẫn là các vấn đề riêng.

## Nguồn

- [NIST CSRC Glossary - Transport Layer Security](https://csrc.nist.gov/glossary/term/transport_layer_security)
