---
title: "Branch là gì?"
category: "git-open-source"
core: true
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# Branch là gì?

Branch - nhánh - là một đường phát triển riêng trong Git để bạn có thể làm thay đổi mà chưa ảnh hưởng trực tiếp tới nhánh khác.

Bạn có thể tạo branch cho một feature hoặc bug fix, commit trên đó rồi merge lại khi thay đổi đã sẵn sàng.

## Tại sao cần nó?

Branch giúp tách công việc đang làm khỏi line ổn định.

```text
main        A ── B ── C
                 \
feature           D ── E
```

## Nó hoạt động thế nào?

Git branch là một reference di chuyển theo [commit](commit.md) mới của line đó. Khi tạo branch từ `main`, ban đầu hai branch có thể cùng trỏ tới một commit; commit mới làm lịch sử phát triển tách ra.

Khi thay đổi sẵn sàng, bạn có thể [merge](merge.md) branch hoặc mở [Pull Request](pull-request.md) để review trước khi merge trên GitHub.

## Ví dụ

```bash
git switch -c add-branch-concept
```

Bạn viết file, commit trên branch đó rồi có thể mở Pull Request.

## Thử ngay

```bash
git branch
git switch -c demo-branch
git branch
```

Dấu `*` cho biết branch hiện tại.

## Dễ nhầm với gì?

**Branch không phải một bản copy vật lý đầy đủ của folder project.** Git triển khai branch bằng reference nhẹ tới commit.

## Đọc tiếp

- [Pull Request là gì?](pull-request.md)
- [Merge là gì?](merge.md)

## Nguồn

- [Pro Git - Branches in a Nutshell](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell)
- [GitHub Docs - Branches](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches)
