---
title: "Virtual Machine là gì?"
category: "cloud-devops"
core: false
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# Virtual Machine là gì?

Virtual Machine - máy ảo, thường viết tắt là **VM** - là một máy tính được mô phỏng bằng phần mềm và có thể chạy hệ điều hành riêng như một máy độc lập.

Nhiều VM có thể cùng chạy trên một máy vật lý nhờ lớp virtualization.

## Tại sao cần nó?

Virtualization cho phép nhiều execution environment chia sẻ cùng hardware vật lý trong khi vẫn được tách thành các VM riêng.

Cloud provider thường có thể cung cấp VM như một loại computing resource, nhưng VM không chỉ tồn tại trong cloud.

## Virtual Machine khác Container thế nào?

Ở mức beginner:

- VM mô phỏng hardware/execution stack và thường chạy guest OS riêng.
- [Container](container.md) dùng operating system virtualization và thường chia sẻ kernel của host.

Vì vậy container thường có lớp abstraction khác VM; không nên coi hai term là cùng một thứ.

## Nguồn

- [NIST CSRC Glossary - Virtual Machine](https://csrc.nist.gov/glossary/term/virtual_machine)
- [NIST SP 800-190 - Application Container Security Guide](https://csrc.nist.gov/pubs/sp/800/190/final)
