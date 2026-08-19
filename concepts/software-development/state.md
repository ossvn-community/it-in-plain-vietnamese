---
title: "State là gì?"
category: "software-development"
core: false
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# State là gì?

State - trạng thái - là tập thông tin mô tả một chương trình hoặc một phần của chương trình đang ở tình trạng nào tại một thời điểm.

Khi state thay đổi, hành vi hoặc kết quả hiển thị của chương trình có thể thay đổi theo.

## Ví dụ

Một ứng dụng nghe nhạc có thể có state như:
- bài hát hiện tại;
- đang phát hay tạm dừng;
- âm lượng;
- vị trí đang phát trong bài.

Khi người dùng bấm Pause, state `playing` thay đổi và giao diện phản ánh trạng thái mới.

## Dễ nhầm với gì?

State không nhất thiết phải là một biến duy nhất. Nó có thể được tạo từ nhiều giá trị nằm ở nhiều phần của chương trình.

## Nguồn

- [Python Documentation - Data model](https://docs.python.org/3/reference/datamodel.html)
