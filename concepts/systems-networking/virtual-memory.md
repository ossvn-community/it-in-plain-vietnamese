---
title: "Virtual Memory là gì?"
category: "systems-networking"
core: false
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# Virtual Memory là gì?

Virtual Memory - bộ nhớ ảo - là cơ chế giúp mỗi process làm việc với một không gian địa chỉ bộ nhớ riêng thay vì trực tiếp sử dụng địa chỉ vật lý của RAM.

Hệ điều hành và phần cứng phối hợp ánh xạ các địa chỉ ảo mà chương trình nhìn thấy tới vùng nhớ vật lý hoặc vùng lưu trữ phù hợp.

## Ví dụ

Hai process có thể đều dùng địa chỉ ảo giống nhau trong code của mình nhưng thực tế được ánh xạ tới các vùng RAM khác nhau. Điều này giúp cách ly process và đơn giản hóa việc quản lý memory.

## Dễ nhầm với gì?

Virtual Memory không có nghĩa đơn giản là “dùng ổ đĩa thay RAM”. Paging ra storage chỉ là một phần có thể có; vai trò cốt lõi là mô hình địa chỉ ảo và ánh xạ bộ nhớ.

## Nguồn

- [Linux Kernel Documentation - Memory Management](https://docs.kernel.org/admin-guide/mm/)
