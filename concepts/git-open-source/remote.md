---
title: "Remote là gì?"
category: "git-open-source"
core: false
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# Remote là gì?

Remote trong Git là tên tham chiếu tới một repository khác mà local repository có thể trao đổi dữ liệu cùng.

Remote phổ biến nhất thường có tên `origin`, nhưng bạn có thể có nhiều remote cho các repository khác nhau.

## Tại sao cần nó?

Git có thể hoạt động local, nhưng khi làm việc cùng người khác bạn thường cần lấy commit từ repository khác hoặc gửi commit của mình lên đó.

Remote lưu địa chỉ để các lệnh như `fetch`, `pull` và `push` biết cần làm việc với repository nào.

## Nó hoạt động thế nào?

```bash
git remote -v
git fetch origin
git push origin main
```

`git fetch origin` lấy dữ liệu mới từ remote về local repository nhưng không tự merge chúng vào branch hiện tại.

## Dễ nhầm với gì?

**Remote không đồng nghĩa với GitHub.** Remote có thể trỏ tới repository trên GitHub hoặc một Git server khác.

**`origin` chỉ là tên mặc định phổ biến**, không phải từ khóa bắt buộc.

## Đọc tiếp

- [Repository là gì?](repository.md)
- [GitHub là gì?](github.md)

## Nguồn

- [Pro Git - Working with Remotes](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes)
- [GitHub Docs - About remote repositories](https://docs.github.com/en/get-started/git-basics/about-remote-repositories)
