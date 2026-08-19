---
title: "Multi-Factor Authentication là gì?"
category: "security"
core: false
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# Multi-Factor Authentication là gì?

Multi-Factor Authentication - xác thực đa yếu tố, thường viết tắt là **MFA** - yêu cầu nhiều hơn một loại bằng chứng để xác thực danh tính.

Ví dụ, hệ thống có thể yêu cầu password cùng một passkey hoặc mã từ thiết bị khác.

## Ví dụ

```text
Password          → something you know
Security key      → something you have
```

Kết hợp hai factor thuộc hai loại khác nhau có thể tạo MFA.

Hai password khác nhau vẫn cùng thuộc nhóm "something you know", nên không tự động trở thành hai factor khác loại.

## Dễ nhầm với gì?

MFA là một cách thực hiện [Authentication](authentication.md), không phải [Authorization](authorization.md).

MFA có thể tăng mức assurance của authentication, nhưng không thay thế authorization hay các security control khác.

## Nguồn

- [NIST SP 800-63B - Authentication and Authenticator Management](https://pages.nist.gov/800-63-4/sp800-63b.html)
- [NIST CSRC Glossary - Multi-Factor Authentication](https://csrc.nist.gov/glossary/term/multi_factor_authentication)
