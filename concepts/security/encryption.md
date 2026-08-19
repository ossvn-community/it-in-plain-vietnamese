---
title: "Encryption là gì?"
category: "security"
core: true
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# Encryption là gì?

Encryption - mã hóa - là cách biến dữ liệu có thể đọc được thành dạng mà người không có key phù hợp khó có thể đọc.

Encryption được dùng để bảo vệ dữ liệu khi lưu trữ hoặc truyền qua mạng.

## Tại sao cần nó?

Encryption được dùng khi cần bảo vệ tính bí mật của dữ liệu, ví dụ dữ liệu đang truyền hoặc dữ liệu lưu trữ.

Việc một hệ thống nên dùng cơ chế encryption nào phụ thuộc vào yêu cầu và ngữ cảnh cụ thể; bài này chỉ giải thích concept.

## Ví dụ

```text
Plaintext
  ↓ encryption + key
Ciphertext
  ↓ decryption + key
Plaintext
```

## Dễ nhầm với gì?

**Encryption không phải Hashing.**

- Encryption được thiết kế để có thể đảo ngược khi có key phù hợp.
- [Hashing](hashing.md) tạo digest và không có bước decryption tương ứng.

## Nguồn

- [NIST CSRC Glossary - Encryption](https://csrc.nist.gov/glossary/term/encryption)
- [NIST SP 800-175B Rev. 1 - Cryptographic Mechanisms](https://csrc.nist.gov/pubs/sp/800/175/b/r1/final)
