---
title: "REST API là gì?"
category: "web"
core: false
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# REST API là gì?

REST API là cách xây API trên Web dựa trên các nguyên tắc của kiến trúc REST và thường sử dụng HTTP để thao tác với resource.

Trong thực tế, client thường làm việc với các URL đại diện cho resource và dùng HTTP method như GET, POST, PUT/PATCH hoặc DELETE.

## Ví dụ

Một API quản lý bài viết có thể dùng:
```text
GET /posts/42
POST /posts
DELETE /posts/42
```
Các endpoint cho phép client đọc, tạo hoặc xóa resource tương ứng.

## Dễ nhầm với gì?

Không phải API dùng HTTP đều là REST API. REST có các ràng buộc kiến trúc; nhiều API ngoài thực tế chỉ “REST-like”.

## Nguồn

- [MDN Glossary - REST](https://developer.mozilla.org/en-US/docs/Glossary/REST)
