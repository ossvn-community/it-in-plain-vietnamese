---
title: "Deployment là gì?"
category: "cloud-devops"
core: false
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# Deployment là gì?

Deployment - triển khai - là quá trình đưa một phiên bản phần mềm tới môi trường mà người dùng hoặc hệ thống khác có thể sử dụng.

Deployment có thể đơn giản như copy file lên server, hoặc phức tạp hơn với pipeline, container, nhiều môi trường và cơ chế rollback.

## Tại sao cần nó?

Code nằm trong repository chưa tự động trở thành application đang chạy cho user.

Giữa source code và production thường có các bước build, package, release và deployment.

## Ví dụ

```text
Source code
   ↓
Build + test
   ↓
Package / release
   ↓
Deploy
   ↓
Running environment
```

Deployment có thể thủ công hoặc được automation hỗ trợ. NIST DevSecOps reference model mô tả deploy phase với automated pipelines cài đặt và cấu hình software trên production infrastructure.

## Liên quan

- [CI/CD là gì?](ci-cd.md)
- [Server là gì?](server.md)
- [Container là gì?](container.md)

## Nguồn

- [NIST NCCoE - DevSecOps Notional Reference Model](https://pages.nist.gov/nccoe-devsecops/notational-reference-model.html)
- [NIST SP 800-204C - Implementation of DevSecOps](https://csrc.nist.gov/pubs/sp/800/204/c/final)
