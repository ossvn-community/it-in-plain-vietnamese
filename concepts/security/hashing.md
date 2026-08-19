---
title: "Hashing là gì?"
category: "security"
core: true
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# Hashing là gì?

Hashing là quá trình biến dữ liệu đầu vào thành một giá trị có độ dài cố định theo một hash function.

Hash thường được dùng để kiểm tra dữ liệu, lập chỉ mục hoặc lưu password theo cách an toàn hơn khi kết hợp thuật toán và cơ chế phù hợp.

## Tại sao cần nó?

Hash thường được dùng khi cần một giá trị đại diện cho dữ liệu, ví dụ để hỗ trợ kiểm tra dữ liệu có thay đổi hay không.

Cách dùng hash an toàn phụ thuộc vào mục đích cụ thể; không phải mọi hash function đều phù hợp cho mọi bài toán security.

## Ví dụ

```text
"hello"
   ↓ hash function
fixed-length digest
```

Chỉ cần input thay đổi, digest có thể thay đổi theo.

## Dễ nhầm với gì?

**Hashing không phải Encryption.**

- [Encryption](encryption.md) có quá trình decryption khi có key phù hợp.
- Hashing không có bước "decrypt hash" để lấy lại input gốc.

## Nguồn

- [NIST CSRC Glossary - Cryptographic Hash Function](https://csrc.nist.gov/glossary/term/Cryptographic_hash_function)
- [NIST FIPS 180-4 - Secure Hash Standard](https://csrc.nist.gov/pubs/fips/180-4/upd1/final)
