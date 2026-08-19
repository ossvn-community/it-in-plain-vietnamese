---
title: "Merge là gì?"
category: "git-open-source"
core: false
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# Merge là gì?

Merge là thao tác kết hợp lịch sử hoặc thay đổi từ một branch vào branch khác.

Trong workflow phổ biến, developer làm việc trên branch riêng rồi merge thay đổi vào `main` sau khi đã review.

## Tại sao cần nó?

[Branch](branch.md) cho phép phát triển thay đổi riêng. Merge là một cách đưa những thay đổi đó trở lại line phát triển khác.

## Nó hoạt động thế nào?

Ví dụ bạn đang ở `main` và muốn đưa thay đổi từ `feature` vào:

```bash
git switch main
git merge feature
```

Nếu Git không thể tự kết hợp thay đổi, merge dừng lại để bạn xử lý conflict trước khi tiếp tục.

## Dễ nhầm với gì?

**Merge không phải Pull Request.** [Pull Request](pull-request.md) là lớp collaboration trên GitHub để đề xuất, review và kiểm tra thay đổi. Merge là thao tác đưa các lịch sử thay đổi lại với nhau.

## Thử ngay

```bash
git log --oneline --graph --all
```

Lệnh này giúp bạn nhìn các branch và lịch sử trước hoặc sau khi merge.

## Đọc tiếp

- [Branch là gì?](branch.md)
- [Pull Request là gì?](pull-request.md)

## Nguồn

- [Git - git-merge Documentation](https://git-scm.com/docs/git-merge)
- [Pro Git - Basic Branching and Merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)
