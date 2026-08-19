---
title: "Memory là gì?"
category: "systems-networking"
core: true
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# Memory là gì?

Memory - bộ nhớ - là nơi máy tính giữ dữ liệu và lệnh mà chương trình cần truy cập trong quá trình chạy.

Khi nói về memory trong lập trình hệ thống, người ta thường nói nhiều tới RAM và không gian bộ nhớ mà process có thể sử dụng.

## Tại sao cần nó?

Chương trình cần memory để giữ dữ liệu đang xử lý, biến, stack và nhiều trạng thái runtime khác.

Hệ điều hành quản lý memory để nhiều process có thể chạy cùng lúc và để address space của process được tách biệt theo cơ chế của hệ thống.

## Process và Thread liên quan thế nào?

Mỗi process thường có virtual address space của riêng nó.

Các thread trong cùng process chia sẻ virtual address space của process, nhưng mỗi thread vẫn có stack riêng cho việc thực thi của nó.

Xem thêm [Process và Thread](process-thread.md).

## Dễ nhầm với gì?

**Memory không chỉ có RAM.** Ứng dụng thường làm việc với virtual addresses; hệ điều hành ánh xạ chúng tới physical memory và có thể dùng cơ chế paging.

Ở level beginner, chỉ cần nhớ: chương trình cần memory để chạy, process có address space, và hệ điều hành quản lý mối quan hệ giữa virtual memory và physical memory.

## Nguồn

- [Microsoft Learn - Virtual Address Spaces](https://learn.microsoft.com/en-us/windows-hardware/drivers/gettingstarted/virtual-address-spaces)
- [Linux man-pages - proc_pid_status](https://man7.org/linux/man-pages/man5/proc_pid_status.5.html)
