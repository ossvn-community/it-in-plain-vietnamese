---
title: "Git là gì?"
category: "git-open-source"
core: true
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# Git là gì?

Git là hệ thống quản lý phiên bản giúp theo dõi lịch sử thay đổi của file và hỗ trợ nhiều người cùng phát triển một project.

Git chạy ngay trên máy của bạn và không phụ thuộc vào GitHub để tạo repository, branch hay commit.

## Tại sao cần nó?

Khi làm project, bạn thường cần biết:

- Đã thay đổi gì?
- Ai thay đổi?
- Khi nào thay đổi?
- Muốn quay lại trạng thái cũ thì sao?
- Hai người có thể làm hai phần khác nhau mà không ghi đè nhau thế nào?

Git lưu lịch sử để giải quyết các câu hỏi đó.

## Nó hoạt động thế nào?

Git làm việc trong một [repository](repository.md) và nhìn lịch sử project như một chuỗi **snapshot**.

```text
Working files
    ↓ git add
Staging area
    ↓ git commit
Git history
```

Mỗi [commit](commit.md) tạo một mốc trong lịch sử. [Branch](branch.md) giúp bạn phát triển một line riêng rồi đưa thay đổi trở lại line khác khi cần.

Vì Git là distributed version control system, việc lưu lịch sử và tạo commit không phụ thuộc vào một server trung tâm luôn phải online.

## Ví dụ

Thay vì tạo nhiều file `README-final-v2...`, Git giúp bạn giữ một file và lưu các mốc thay đổi bằng commit.

## Thử ngay

```bash
git --version
mkdir git-demo
cd git-demo
git init
git status
```

`git init` biến folder hiện tại thành một Git repository mới.

## Dễ nhầm với gì?

**Git không phải GitHub.** Git là version control system. GitHub là platform có thể host Git repositories và thêm công cụ collaboration.

## Đọc tiếp

- [Repository là gì?](repository.md)
- [Commit là gì?](commit.md)
- [Branch là gì?](branch.md)

## Nguồn

- [Pro Git - What is Git?](https://git-scm.com/book/en/v2/Getting-Started-What-is-Git)
- [GitHub Docs - About Git](https://docs.github.com/en/get-started/using-git/about-git)
