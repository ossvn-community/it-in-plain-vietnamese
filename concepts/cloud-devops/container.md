---
title: "Container là gì?"
category: "cloud-devops"
core: true
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# Container là gì?

Container là cách đóng gói application cùng những dependency cần thiết để nó có thể chạy trong một môi trường được cô lập ở mức hệ điều hành.

Container giúp môi trường chạy nhất quán hơn giữa máy developer, CI và server triển khai.

## Tại sao cần nó?

Team thường muốn application chạy nhất quán qua nhiều environment và có thể được build/deploy tự động.

Container là một cách phổ biến để đóng gói workload cho mục tiêu đó.

## Container khác Virtual Machine thế nào?

Ở mức beginner:

- Container dùng operating system virtualization và thường chia sẻ kernel của host.
- [Virtual Machine](virtual-machine.md) mô phỏng một execution environment đầy đủ hơn và có guest operating system riêng.

Hai công nghệ đều liên quan tới isolation và virtualization nhưng ở lớp khác nhau.

## Ví dụ

Một container image có thể đóng gói application cùng runtime và libraries cần thiết để chạy application đó trên container platform tương thích.

## Đọc tiếp

- [Virtual Machine là gì?](virtual-machine.md)
- [Process và Thread là gì?](../systems-networking/process-thread.md)

## Nguồn

- [NIST SP 800-190 - Application Container Security Guide](https://csrc.nist.gov/pubs/sp/800/190/final)
- [NIST CSRC Glossary - Container](https://csrc.nist.gov/glossary/term/container)
