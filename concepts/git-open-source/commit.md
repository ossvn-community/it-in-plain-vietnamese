---
title: "Commit là gì?"
category: "git-open-source"
core: true
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# Commit là gì?

Commit là một mốc lưu thay đổi trong lịch sử Git.

Mỗi commit ghi lại trạng thái thay đổi cùng metadata như tác giả và thời điểm, giúp project có thể xem lại mình đã thay đổi gì theo thời gian.

## Tại sao cần nó?

Commit chia lịch sử của một [repository](repository.md) thành các mốc có ý nghĩa để bạn có thể review, so sánh hoặc quay lại khi cần.

## Nó hoạt động thế nào?

```text
Sửa file
  ↓
git add
  ↓
Staging area
  ↓
git commit
  ↓
Commit mới trong history
```

Theo mặc định, `git commit` ghi nội dung đang ở staging area thành commit mới và gắn commit message mô tả thay đổi.

Các commit mới thường làm [branch](branch.md) hiện tại di chuyển tới commit mới đó.

## Ví dụ

```bash
git add README.md concepts/git-open-source/git.md
git commit -m "docs: clarify Git concept"
```

## Thử ngay

```bash
git status
git diff
git add README.md
git diff --staged
```

## Dễ nhầm với gì?

**Commit không phải save file.** Save ghi file xuống disk; commit ghi một mốc vào Git history.

**Commit không phải push.** Commit được tạo trong local repository; `git push` gửi commit tới remote.

## Đọc tiếp

- [Branch là gì?](branch.md)
- [Remote là gì?](remote.md)

## Nguồn

- [Git - git-commit Documentation](https://git-scm.com/docs/git-commit)
- [Pro Git - What is Git?](https://git-scm.com/book/en/v2/Getting-Started-What-is-Git)
