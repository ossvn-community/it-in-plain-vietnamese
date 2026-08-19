---
title: "Authorization là gì?"
category: "security"
core: true
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# Authorization là gì?

Authorization - phân quyền - là quá trình quyết định một người hoặc hệ thống đã được xác định danh tính thì được phép làm gì.

Authentication trả lời “bạn là ai?”, còn authorization trả lời “bạn được quyền làm gì?”.

## Tại sao cần nó?

Hai user đều có thể đăng nhập thành công nhưng có quyền khác nhau.

Ví dụ, user thường có thể đọc profile của mình, trong khi admin có thể có thêm quyền quản lý tài khoản khác.

## Nó hoạt động thế nào?

Ở mức đơn giản:

```text
Request
  ↓
Entity đã được nhận diện
  ↓
Kiểm tra quyền / policy
  ↓
Cho phép hoặc từ chối action
```

Cách biểu diễn quyền có thể khác nhau giữa các hệ thống.

## Dễ nhầm với gì?

**Authorization không phải Authentication.**

- [Authentication](authentication.md) xác minh danh tính.
- Authorization kiểm tra quyền của entity đối với action hoặc resource.

Authentication thường xảy ra trước authorization, nhưng hai khái niệm giải quyết hai câu hỏi khác nhau.

## Đọc tiếp

- [Least Privilege là gì?](least-privilege.md)

## Nguồn

- [NIST CSRC Glossary - Authorization](https://csrc.nist.gov/glossary/term/authorization)
- [OWASP Cheat Sheet - Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)
