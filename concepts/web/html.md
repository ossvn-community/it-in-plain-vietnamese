---
title: "HTML là gì?"
category: "web"
core: false
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# HTML là gì?

HTML - HyperText Markup Language - là ngôn ngữ đánh dấu dùng để mô tả cấu trúc và ý nghĩa của nội dung trên trang Web.

HTML cho trình duyệt biết đâu là heading, đoạn văn, link, ảnh, form và các thành phần nội dung khác.

## Nó hoạt động thế nào?

HTML dùng các element để mô tả nội dung:

```html
<h1>IT in Plain Vietnamese</h1>
<p>Giải thích concept IT bằng tiếng Việt đơn giản.</p>
<a href="/concepts/">Xem concepts</a>
```

[Browser](browser.md) parse HTML thành cấu trúc trong bộ nhớ rồi dùng cấu trúc đó cùng CSS, JavaScript và các tài nguyên khác để render trang.

## Tại sao cần nó?

HTML định nghĩa phần nội dung và cấu trúc cơ bản của web page. CSS thường xử lý presentation, còn JavaScript thường xử lý behavior và interaction.

## Thử ngay

Tạo file `hello.html`:

```html
<!doctype html>
<html lang="vi">
  <body>
    <h1>Xin chào Web</h1>
  </body>
</html>
```

Mở file bằng browser để xem kết quả.

## Dễ nhầm với gì?

**HTML không phải HTTP.** HTML là một format nội dung; [HTTP](http.md) là protocol có thể được dùng để truyền HTML và nhiều loại dữ liệu khác.

## Đọc tiếp

- [Browser là gì?](browser.md)
- [HTTP là gì?](http.md)

## Nguồn

- [WHATWG - HTML Standard](https://html.spec.whatwg.org/)
- [MDN - Structuring content with HTML](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content)
