---
title: "Authentication là gì?"
category: "security"
core: true
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# Authentication là gì?

Authentication - xác thực - là quá trình kiểm tra một người hoặc hệ thống có đúng là danh tính mà họ khai báo hay không.

Đăng nhập bằng password, passkey hoặc một yếu tố xác thực khác đều là ví dụ của authentication.

## Tại sao cần nó?

Trước khi hệ thống cho một entity truy cập tài nguyên riêng, hệ thống thường cần xác minh danh tính của entity đó.

Authentication có thể dùng password, security token, cryptographic key, biometric hoặc nhiều yếu tố kết hợp.

## Ví dụ

Bạn nhập username và password để đăng nhập một ứng dụng. Nếu hệ thống xác minh thông tin đăng nhập hợp lệ, bước authentication thành công.

Sau đó hệ thống vẫn cần quyết định bạn được phép làm gì. Đó là [Authorization](authorization.md).

## Dễ nhầm với gì?

**Authentication không phải Authorization.**

- Authentication: xác minh danh tính.
- Authorization: xác định quyền truy cập hoặc hành động được phép.

Đăng nhập thành công không có nghĩa là user được phép truy cập mọi resource.

## Đọc tiếp

- [Authorization là gì?](authorization.md)
- [Multi-Factor Authentication là gì?](multi-factor-authentication.md)

## Nguồn

- [NIST CSRC Glossary - Authentication](https://csrc.nist.gov/glossary/term/authentication)
- [OWASP Cheat Sheet - Authentication](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)
