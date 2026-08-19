---
title: "Least Privilege là gì?"
category: "security"
core: false
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# Least Privilege là gì?

Least Privilege - nguyên tắc đặc quyền tối thiểu - yêu cầu mỗi người, account hoặc service chỉ được cấp những quyền cần thiết cho công việc của nó.

Giảm quyền thừa giúp giới hạn thiệt hại nếu account bị dùng sai hoặc bị xâm nhập.

## Tại sao cần nó?

Quyền truy cập càng rộng thì một lỗi hoặc tài khoản bị compromise có thể tác động tới nhiều tài nguyên hơn.

Least Privilege giúp giới hạn phạm vi quyền thay vì mặc định cấp nhiều quyền hơn nhu cầu thực tế.

## Ví dụ

Một service chỉ cần đọc một bucket dữ liệu thì quyền chỉ đọc phù hợp hơn quyền quản trị toàn bộ hệ thống lưu trữ.

Quyền cụ thể vẫn phải được xác định theo chức năng và context thực tế của hệ thống.

## Liên quan

Least Privilege là một nguyên tắc thường được dùng khi thiết kế [Authorization](authorization.md).

## Nguồn

- [NIST CSRC Glossary - Least Privilege](https://csrc.nist.gov/glossary/term/least_privilege)
- [OWASP Cheat Sheet - Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)
