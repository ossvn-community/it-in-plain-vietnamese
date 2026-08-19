---
title: "Cookie là gì?"
category: "web"
core: false
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# Cookie là gì?

Cookie là một mẩu dữ liệu nhỏ mà server có thể yêu cầu trình duyệt lưu và gửi lại trong các request phù hợp.

Cookie thường được dùng để duy trì session đăng nhập, ghi nhớ lựa chọn hoặc phục vụ một số nhu cầu theo dõi.

## Ví dụ

Sau khi đăng nhập, server có thể gửi một cookie chứa session identifier. Ở các request tiếp theo tới cùng website, trình duyệt gửi cookie phù hợp để server nhận ra session.

## Dễ nhầm với gì?

Cookie không phải nơi phù hợp để lưu mọi dữ liệu của ứng dụng. Cookie được gửi kèm request theo các quy tắc của nó, còn Web Storage là một cơ chế lưu dữ liệu phía trình duyệt với cách sử dụng khác.

## Nguồn

- [MDN - Using HTTP cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Cookies)
