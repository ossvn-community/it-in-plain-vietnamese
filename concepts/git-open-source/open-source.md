---
title: "Open-source là gì?"
category: "git-open-source"
core: false
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# Open-source là gì?

Open Source - mã nguồn mở - là cách phát hành phần mềm trong đó source code được cung cấp theo một license cho phép người khác sử dụng, xem, sửa đổi và phân phối theo các điều kiện của license đó.

Open source không chỉ là “code được nhìn thấy công khai”; quyền sử dụng cụ thể phụ thuộc license.

## Tại sao cần nó?

Nếu không có license rõ, người khác không biết họ thực sự được phép làm gì với code.

Open-source license tạo một bộ quyền và điều kiện chung để người khác có thể học, dùng, sửa hoặc xây tiếp mà không phải xin phép từng lần.

## Nó hoạt động thế nào?

Một project open-source thường có:

```text
Source code
    +
Open-source license
    ↓
Người khác có quyền dùng / sửa / phân phối
trong phạm vi license
```

Open Source Initiative (OSI) nhấn mạnh rằng open source không chỉ là quyền đọc source code. License còn phải đáp ứng các tiêu chí như cho phép redistribution và derived works, không phân biệt người dùng hay lĩnh vực sử dụng.

## Ví dụ

Một project dùng MIT License cho phép người khác dùng, copy, sửa, merge, publish, distribute và bán phần mềm, miễn họ giữ copyright notice và license notice theo điều kiện của MIT.

Ngược lại, một public repository trên GitHub nhưng không có license rõ không tự động trao cho người khác đầy đủ các quyền open-source.

## Thử ngay

Mở một repository public bất kỳ và tìm file:

```text
LICENSE
LICENSE.md
COPYING
```

Đừng chỉ nhìn xem source có public hay không. Hãy xem license nói bạn được phép làm gì.

## Dễ nhầm với gì?

**Open-source không đồng nghĩa với miễn phí về giá.** Open-source software vẫn có thể được bán hoặc dùng trong sản phẩm thương mại.

**Source-available cũng không nhất thiết là open-source.** Một license có thể cho bạn xem source nhưng hạn chế các quyền mà Open Source Definition yêu cầu.

## Nguồn

- [Open Source Initiative - The Open Source Definition](https://opensource.org/osd)
- [Open Source Initiative - Frequently Answered Questions](https://opensource.org/faq)
