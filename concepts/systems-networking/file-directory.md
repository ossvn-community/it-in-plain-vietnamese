---
title: "File và Directory là gì?"
category: "systems-networking"
core: false
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# File và Directory là gì?

**File - tệp tin** là một đơn vị dùng để lưu dữ liệu trên máy tính, thường có tên để người dùng và chương trình có thể tìm lại.

**Directory - thư mục, hay folder** là nơi dùng để tổ chức các file và các directory khác.

## File

Một file có thể chứa nhiều loại nội dung khác nhau, ví dụ:

- Văn bản: `notes.txt`
- Hình ảnh: `photo.jpg`
- Video: `video.mp4`
- Mã nguồn: `app.py`

Tên file thường có phần mở rộng như `.txt`, `.jpg` hoặc `.py`, nhưng phần mở rộng không phải là điều duy nhất quyết định bản chất của file.

## Directory

Directory giúp nhóm và sắp xếp file thay vì để tất cả ở cùng một chỗ.

Một directory cũng có thể chứa directory con, tạo thành cấu trúc dạng cây.

## Ví dụ

```text
project/
├── README.md
└── src/
    └── app.py
```

`README.md` và `app.py` là file. `project` và `src` là directory.

Chuỗi như `src/app.py` là một **path - đường dẫn**, dùng để chỉ vị trí của file trong cấu trúc thư mục.

## So sánh

- File chứa dữ liệu cụ thể.
- Directory dùng để tổ chức file và directory khác.

## Thử ngay

Trên Linux hoặc macOS:

```bash
pwd
ls
mkdir demo
touch demo/hello.txt
ls demo
```

## Nguồn

- [POSIX.1-2024 - Definitions](https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap03.html)
- [POSIX.1-2024 - Pathname Resolution](https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap04.html)
