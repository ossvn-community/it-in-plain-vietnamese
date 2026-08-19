---
title: "Secret là gì?"
category: "security"
core: false
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# Secret là gì?

Secret là thông tin nhạy cảm mà hệ thống dùng để chứng minh danh tính, truy cập dịch vụ hoặc thực hiện thao tác bảo mật.

Ví dụ thường gặp gồm API key, password, private key và access token.

## Ví dụ

Một application gọi dịch vụ bên ngoài bằng API key. Key đó không nên hard-code vào source code public; thường nó được cấp qua secret manager hoặc biến môi trường có kiểm soát.

## Dễ nhầm với gì?

Secret không giống configuration thông thường. Một URL public có thể là config; token cho phép truy cập hệ thống là secret và cần được bảo vệ chặt hơn.

## Nguồn

- [OWASP - Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)
