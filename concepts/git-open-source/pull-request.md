---
title: "Pull Request là gì?"
category: "git-open-source"
core: true
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# Pull Request là gì?

Pull Request - thường viết tắt là **PR** - là cách đề xuất một tập thay đổi để người khác xem, thảo luận và quyết định có đưa vào branch đích hay không.

PR thường gắn với một branch và cho thấy diff giữa thay đổi được đề xuất với code hiện tại.

## Tại sao cần nó?

[Branch](branch.md) giúp tách thay đổi. Pull Request thêm bước collaboration để người khác xem và kiểm tra thay đổi trước khi đưa chúng vào branch đích.

Đây cũng là flow contribution chính của OSSVN.

## Nó hoạt động thế nào?

```text
Create branch
    ↓
Make commits
    ↓
Push branch
    ↓
Open Pull Request
    ↓
Review + Checks
    ↓
Merge
```

Reviewer có thể xem file changed, comment, yêu cầu sửa hoặc approve. Automated checks cũng có thể chạy trước khi [merge](merge.md).

## Ví dụ

Bạn sửa typo trên branch `fix-git-typo`, rồi mở PR `fix-git-typo -> main` để maintainer review.

## Thử ngay

Mở một Pull Request trên GitHub và xem `Conversation`, `Commits`, `Checks`, `Files changed`.

## Dễ nhầm với gì?

**Pull Request không phải command hay khái niệm cốt lõi của Git.** Đây là collaboration feature của [GitHub](github.md).

**Mở PR không có nghĩa là thay đổi đã vào `main`.** PR chỉ là đề xuất cho tới khi được merge.

## Đọc tiếp

- [Merge là gì?](merge.md)
- [GitHub là gì?](github.md)

## Nguồn

- [GitHub Docs - About pull requests](https://docs.github.com/en/pull-requests/get-started/about-pull-requests)
- [GitHub Docs - Pull request quickstart](https://docs.github.com/en/pull-requests/get-started/pull-request-quickstart)
