---
title: "Process và Thread là gì?"
category: "systems-networking"
core: true
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# Process và Thread là gì?

**Process - tiến trình** là một chương trình đang chạy cùng các tài nguyên mà hệ điều hành cấp cho nó.

**Thread - luồng** là một luồng thực thi nằm bên trong process. Một process có thể có một hoặc nhiều thread cùng thực hiện công việc.

## Process

Khi một chương trình được chạy, hệ điều hành có thể tạo một process cho chương trình đó.

Process có các tài nguyên phục vụ việc chạy chương trình, trong đó có không gian địa chỉ bộ nhớ và các thông tin mà hệ điều hành dùng để quản lý nó.

Một file chương trình nằm trên ổ đĩa chưa phải là process. Process chỉ tồn tại khi chương trình đang được thực thi.

## Thread

Thread là phần thực hiện các lệnh bên trong process.

Các thread trong cùng một process chia sẻ nhiều tài nguyên của process, nhưng mỗi thread vẫn có trạng thái thực thi riêng.

Ví dụ, một ứng dụng có thể dùng một thread cho giao diện và các worker thread cho những công việc khác.

## Điểm khác biệt chính

```text
Process
├── Thread 1
├── Thread 2
└── Thread 3
```

- Process là môi trường chứa tài nguyên để chương trình chạy.
- Thread là luồng thực thi bên trong process.
- Nhiều thread trong cùng process có thể chia sẻ nhiều tài nguyên với nhau.

## Dễ nhầm với gì?

**Process không đồng nghĩa với program file.** File executable nằm trên disk; process là một instance đang chạy.

**Thread không phải một process nhỏ hoàn toàn độc lập.** Các thread trong cùng process chia sẻ nhiều tài nguyên của process.

## Đọc tiếp

- [Memory là gì?](memory.md)
- [Operating System là gì?](operating-system.md)

## Nguồn

- [Microsoft Learn - About Processes and Threads](https://learn.microsoft.com/en-us/windows/win32/procthread/about-processes-and-threads)
- [POSIX.1-2024 - Threads](https://pubs.opengroup.org/onlinepubs/9799919799/functions/V2_chap02.html)
