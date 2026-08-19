---
title: "GitHub là gì?"
category: "git-open-source"
core: false
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# GitHub là gì?

GitHub là nền tảng online để lưu Git repository và cộng tác quanh source code.

Ngoài việc host repository, GitHub cung cấp Pull Request, Issue, Actions, review code và nhiều công cụ hỗ trợ quy trình phát triển.

## Tại sao cần nó?

Git giúp bạn quản lý lịch sử project trên máy. GitHub cung cấp nơi chung để chia sẻ repository, cộng tác, review và chạy automation.

## Nó hoạt động thế nào?

```text
Máy của bạn
Git repository
    ↓ push
GitHub repository
    ├── Pull Requests
    ├── Issues
    ├── Reviews
    └── Actions / automation
```

Bạn vẫn có thể commit bằng Git khi offline. Khi có mạng, bạn có thể push commit lên GitHub.

## Ví dụ

Bạn tạo branch `fix-typo`, commit trên máy, push branch lên GitHub rồi mở Pull Request để review trước khi merge vào `main`.

## Thử ngay

Mở một repository trên GitHub và tìm `Code`, `Issues`, `Pull requests`, `Actions`.

## Dễ nhầm với gì?

**GitHub không phải Git.** Git là version control system. GitHub là một platform cung cấp hosting và collaboration quanh Git repositories.

## Nguồn

- [GitHub Docs - About Git](https://docs.github.com/en/get-started/using-git/about-git)
- [GitHub Docs - About repositories](https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories)
