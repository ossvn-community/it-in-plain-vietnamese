---
title: "Load Balancer là gì?"
category: "cloud-devops"
core: false
status: "draft"
last_reviewed: "2026-08-19"
reviewers: []
---

# Load Balancer là gì?

Load Balancer - bộ cân bằng tải - là thành phần phân phối request hoặc connection tới nhiều backend.

Mục tiêu thường là tránh dồn toàn bộ traffic vào một máy và giúp hệ thống tiếp tục phục vụ khi một backend gặp vấn đề.

## Ví dụ

Nếu một website chạy trên ba server, load balancer có thể nhận request từ người dùng rồi chuyển từng request tới server phù hợp dựa trên thuật toán và trạng thái health check.

## Dễ nhầm với gì?

Load Balancer không tự làm application nhanh trong mọi trường hợp. Backend, database và kiến trúc phía sau vẫn có thể là bottleneck.

## Nguồn

- [NGINX Documentation - HTTP Load Balancing](https://docs.nginx.com/nginx/admin-guide/load-balancer/http-load-balancer/)
