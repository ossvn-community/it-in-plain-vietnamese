---
title: "DNS là gì?"
category: "web"
core: true
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# DNS là gì?

DNS - **Domain Name System** - là hệ thống giúp tìm thông tin gắn với một tên miền. Trên Web, một việc rất phổ biến của DNS là tìm địa chỉ IP tương ứng với tên như `example.com`.

Một cách hình dung đơn giản, DNS giống như danh bạ của Internet: bạn nhớ một cái tên dễ đọc, còn hệ thống giúp tìm thông tin cần thiết để máy tính biết nơi cần kết nối.

## Vai trò

Tên miền như `example.com` thường dễ nhớ hơn một địa chỉ IP.

DNS cho phép website và nhiều dịch vụ Internet sử dụng tên thay vì yêu cầu người dùng ghi nhớ địa chỉ mạng trực tiếp.

DNS còn lưu nhiều loại thông tin khác ngoài địa chỉ IP, nhưng người mới có thể bắt đầu từ việc hiểu cơ chế phân giải tên này.

## Cách hoạt động cơ bản

Ở mức đơn giản:

1. Bạn nhập một địa chỉ có tên miền vào browser.
2. Thiết bị hỏi DNS để tìm thông tin tương ứng với tên đó.
3. DNS trả về câu trả lời, chẳng hạn địa chỉ IP của server.
4. Client dùng thông tin đó để tiếp tục kết nối tới server.

```text
example.com
    ↓ DNS query
DNS resolver / name servers
    ↓ DNS answer
IP address
```

DNS là hệ thống phân tán và có caching, vì vậy một truy vấn thực tế có thể đi qua nhiều thành phần trước khi có câu trả lời cuối cùng.

## Thử ngay

```bash
nslookup example.com
```

Lệnh này hỏi DNS để lấy thông tin về domain.

## Dễ nhầm với gì?

**DNS không tải website.** DNS giúp tìm thông tin về tên. Sau đó [client](client-server.md) mới kết nối và trao đổi dữ liệu với server bằng protocol phù hợp như HTTP.

## Đọc tiếp

- [Client và Server là gì?](client-server.md)
- [HTTP là gì?](http.md)

## Nguồn

- [RFC 1034 - Domain Names: Concepts and Facilities](https://www.rfc-editor.org/rfc/rfc1034)
- [RFC 1035 - Domain Names: Implementation and Specification](https://www.rfc-editor.org/rfc/rfc1035)
