---
title: "Filesystem là gì?"
category: "systems-networking"
core: false
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# Filesystem là gì?

Filesystem - hệ thống tệp - là cách hệ điều hành tổ chức, đặt tên, lưu và truy cập file cùng directory trên thiết bị lưu trữ.

Nhờ filesystem, chương trình có thể làm việc với đường dẫn như `/home/nam/note.txt` thay vì phải tự biết dữ liệu nằm ở vị trí vật lý nào trên ổ đĩa.

## Ví dụ

Khi bạn tạo một file trong thư mục `Documents`, filesystem lưu metadata cần thiết và ánh xạ tên file tới dữ liệu của nó. Các filesystem như ext4, NTFS hoặc APFS có cách triển khai khác nhau nhưng đều giải quyết bài toán tổ chức dữ liệu.

## Dễ nhầm với gì?

Filesystem không phải một folder. Folder/directory là một phần của cấu trúc mà filesystem quản lý.

## Nguồn

- [Linux Kernel Documentation - Virtual File System](https://docs.kernel.org/filesystems/vfs.html)
