---
title: "Repository là gì?"
category: "git-open-source"
core: true
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# Repository là gì?

Repository - kho mã nguồn, thường gọi ngắn là **repo** - là nơi Git lưu project cùng lịch sử thay đổi của nó.

Một repository gồm các file đang làm việc và dữ liệu Git cần để theo dõi commit, branch, tag và lịch sử.

## Tại sao cần nó?

Project không chỉ có source code hiện tại. Repository giúp [Git](git.md) quản lý file, [commit](commit.md), [branch](branch.md) và lịch sử của project như một đơn vị.

## Nó hoạt động thế nào?

```text
my-project/
├── README.md
├── src/
└── .git/   ← metadata + Git history cục bộ
```

Khi clone một Git repository, bạn lấy repository về máy để xem file và làm việc với lịch sử Git.

Một repository có thể liên kết với một [remote](remote.md) để trao đổi commit với repository ở nơi khác, ví dụ GitHub.

## Ví dụ

`ossvn-community/it-in-plain-vietnamese` là một repository chứa concept và lịch sử thay đổi của project.

## Thử ngay

```bash
git status
git log --oneline -5
```

## Dễ nhầm với gì?

**Folder bình thường chưa chắc là Git repository.** Folder trở thành Git repository khi được khởi tạo bằng Git hoặc clone từ một repository khác.

## Đọc tiếp

- [Commit là gì?](commit.md)
- [Branch là gì?](branch.md)
- [Remote là gì?](remote.md)

## Nguồn

- [GitHub Docs - About repositories](https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories)
- [GitHub Docs - About Git](https://docs.github.com/en/get-started/using-git/about-git)
