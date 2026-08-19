---
title: "ETL là gì?"
category: "data"
core: false
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# ETL là gì?

ETL là viết tắt của **Extract, Transform, Load** - lấy dữ liệu, biến đổi dữ liệu rồi nạp vào hệ thống đích.

ETL thường được dùng khi cần gom dữ liệu từ nhiều nguồn về data warehouse hoặc hệ thống phân tích.

## Ví dụ

Một pipeline có thể:
1. Extract đơn hàng từ database và file CSV.
2. Transform để chuẩn hóa ngày tháng, tiền tệ và tên cột.
3. Load dữ liệu đã chuẩn hóa vào data warehouse.

## Dễ nhầm với gì?

ETL không phải cách duy nhất xây data pipeline. Một số hệ thống dùng ELT - load dữ liệu trước rồi transform ở hệ thống đích.

## Nguồn

- [AWS - What is ETL?](https://aws.amazon.com/what-is/etl/)
