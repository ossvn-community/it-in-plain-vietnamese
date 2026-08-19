---
title: "CI/CD là gì?"
category: "cloud-devops"
core: true
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# CI/CD là gì?

CI/CD là nhóm thực hành tự động hóa việc tích hợp thay đổi code, kiểm tra và đưa phần mềm tới môi trường sử dụng.

**CI - Continuous Integration** tập trung vào việc tích hợp và kiểm tra thay đổi thường xuyên. **CD** thường nói tới việc tự động chuẩn bị hoặc triển khai phần mềm sau đó.

## Tại sao cần nó?

Khi các bước build, test và release được thực hiện lặp lại bằng pipeline, team có thể giảm bớt thao tác thủ công và tạo feedback sớm hơn cho mỗi thay đổi.

Pipeline cụ thể phụ thuộc project; CI/CD không bắt buộc một tool hay cloud provider nhất định.

## Flow đơn giản

```text
Code change
   ↓
Build
   ↓
Test
   ↓
Package
   ↓
Deliver / Deploy
```

Continuous Delivery và Continuous Deployment có thể khác nhau ở cách thay đổi được đưa vào production, vì vậy cần đọc định nghĩa của workflow đang dùng thay vì mặc định hai term luôn giống nhau.

## Đọc tiếp

- [Deployment là gì?](deployment.md)
- [Infrastructure as Code là gì?](infrastructure-as-code.md)

## Nguồn

- [NIST SP 800-204C - Implementation of DevSecOps](https://csrc.nist.gov/pubs/sp/800/204/c/final)
- [NIST SP 800-204D - Software Supply Chain Security in CI/CD Pipelines](https://csrc.nist.gov/pubs/sp/800/204/d/final)
