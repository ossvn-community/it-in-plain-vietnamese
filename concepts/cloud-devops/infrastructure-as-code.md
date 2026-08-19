---
title: "Infrastructure as Code là gì?"
category: "cloud-devops"
core: true
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# Infrastructure as Code là gì?

Infrastructure as Code - thường viết tắt là **IaC** - là cách mô tả và quản lý hạ tầng bằng file cấu hình hoặc code thay vì chỉ thao tác thủ công.

Nhờ đó cấu hình server, network hoặc cloud resource có thể được review, lưu lịch sử và tạo lại theo quy trình nhất quán.

## Tại sao cần nó?

Nếu hạ tầng chỉ được tạo bằng thao tác thủ công, việc lặp lại cùng một cấu hình ở nhiều environment dễ phụ thuộc vào trí nhớ và thao tác của con người.

IaC cho phép mô tả hạ tầng thành artifact có thể lưu, review và đưa qua workflow tự động giống các loại code khác.

## Ví dụ

Một file IaC có thể mô tả:

```text
- network cần tạo
- server/resource cần provision
- storage cần cấu hình
```

Tool IaC đọc mô tả đó và thực hiện các thay đổi tương ứng theo khả năng của platform.

## Dễ nhầm với gì?

IaC không đồng nghĩa với một sản phẩm cụ thể. Terraform, CloudFormation hoặc các tool khác là implementation; concept IaC rộng hơn các tool đó.

## Đọc tiếp

- [Cloud Computing là gì?](cloud-computing.md)
- [CI/CD là gì?](ci-cd.md)

## Nguồn

- [NIST SP 800-204C - Implementation of DevSecOps](https://csrc.nist.gov/pubs/sp/800/204/c/final)
- [NIST CSRC Glossary - Infrastructure as Code](https://csrc.nist.gov/glossary/term/infrastructure_as_code)
