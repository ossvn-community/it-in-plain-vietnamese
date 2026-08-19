---
title: "Dependency là gì?"
category: "software-development"
core: false
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# Dependency là gì?

Dependency - phụ thuộc - là phần mềm, package hoặc component mà project cần để build, chạy hoặc phát triển.

Khi project dựa vào dependency, thay đổi về phiên bản hoặc khả năng tương thích của dependency có thể ảnh hưởng tới project.

## Ví dụ

Một web app Python dùng package `requests` để gọi HTTP có thể khai báo `requests` là dependency. Công cụ quản lý package sẽ dựa vào khai báo đó để cài phiên bản phù hợp.

## Dễ nhầm với gì?

Dependency không nhất thiết là code bạn tự viết. Nó thường là package bên ngoài, nhưng cũng có thể là component nội bộ giữa các phần của cùng hệ thống.

## Nguồn

- [Python Packaging User Guide - Dependency specifiers](https://packaging.python.org/en/latest/specifications/dependency-specifiers/)
