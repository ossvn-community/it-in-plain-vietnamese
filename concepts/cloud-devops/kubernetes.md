---
title: "Kubernetes là gì?"
category: "cloud-devops"
core: false
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# Kubernetes là gì?

Kubernetes là một nền tảng open source để triển khai và quản lý các application chạy bằng container trên nhiều máy.

Nó giúp tự động hóa những việc như đặt container lên node, giữ số lượng instance mong muốn, cập nhật phiên bản và cung cấp cơ chế networking/service discovery.

## Ví dụ

Bạn muốn chạy 3 bản sao của một web service. Kubernetes có thể giữ trạng thái mong muốn là 3 replicas và tạo lại pod nếu một bản sao bị dừng ngoài ý muốn.

## Dễ nhầm với gì?

Kubernetes không phải container runtime và không bắt buộc cho mọi project dùng container. Với hệ thống nhỏ, cách triển khai đơn giản hơn có thể phù hợp hơn.

## Nguồn

- [Kubernetes Documentation - Concepts](https://kubernetes.io/docs/concepts/)
