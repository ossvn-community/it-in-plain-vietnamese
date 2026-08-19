---
title: "Text Encoding là gì?"
category: "systems-networking"
core: false
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# Text Encoding là gì?

Text Encoding - mã hóa văn bản - là quy ước biến ký tự thành các giá trị số/byte để máy tính có thể lưu và truyền văn bản.

Nếu hai chương trình hiểu cùng một chuỗi byte theo hai encoding khác nhau, chữ có thể hiển thị sai.

## Ví dụ

UTF-8 là một encoding rất phổ biến của Unicode. Cùng một chữ tiếng Việt như `ế` được biểu diễn thành byte theo quy tắc UTF-8 để file, trình duyệt và chương trình có thể trao đổi thống nhất.

## Dễ nhầm với gì?

Unicode và UTF-8 không hoàn toàn đồng nghĩa. Unicode xác định tập ký tự và code point; UTF-8 là một cách encode các code point đó thành byte.

## Nguồn

- [Unicode Standard - Recent Releases](https://www.unicode.org/releases/)
- [Unicode - UTF-8](https://www.unicode.org/faq/utf_bom.html)
