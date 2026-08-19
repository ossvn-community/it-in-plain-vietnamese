# Contributing to IT in Plain Vietnamese

Bạn có thể:

- Sửa typo hoặc link.
- Làm câu dễ hiểu hơn mà không đổi nghĩa.
- Thêm ví dụ hoặc nguồn tốt hơn.
- Viết concept mới.

Không cần xin membership trước khi mở PR.

## Sửa concept có sẵn

1. Chỉ sửa đúng scope.
2. Nếu đổi claim kỹ thuật, thêm hoặc cập nhật nguồn.
3. Giữ `status: draft` nếu chưa có review phù hợp.

## Viết concept mới

1. Đọc phần `Chọn concept` trong [CONTENT_GUIDE.md](CONTENT_GUIDE.md) và kiểm tra concept có thực sự cần một page riêng.
2. Copy `concepts/_template.md`.
3. Chọn đúng `category` và giữ `core: false` theo mặc định.
4. Viết kết luận chính trước.
5. Thêm ví dụ và `Thử ngay` nếu phù hợp.
6. Có ít nhất một nguồn đáng tin cậy cho claim kỹ thuật.
7. Mở PR chỉ tập trung vào concept đó.

Nếu PR thay đổi nhóm 5 khái niệm nên đọc trước, giải thích ngắn lý do chọn hoặc thay concept và không quyết định chỉ dựa trên độ nổi tiếng hoặc vote.

## Trước khi mở PR

### 1. Kiểm tra diff

```bash
git status --short
git diff --check
git diff
```

### 2. Chạy automated checks

Từ root của repository:

```bash
python scripts/validate.py
python scripts/check_links.py
```

### 3. Kiểm tra thủ công

- Preview các file Markdown đã sửa.
- Với claim kỹ thuật đã sửa, mở từng link trong section `Nguồn` và xác nhận source support claim đó.
- Nếu sửa `category`, `core` hoặc knowledge map, kiểm tra vị trí concept trong `concepts/README.md` khớp metadata của concept.

### 4. Kết quả mong đợi

- `git diff --check` exit code bằng `0`.
- `python scripts/validate.py` in `Concept validation passed (... files).`.
- `python scripts/check_links.py` in `Internal Markdown links passed.`.
- Markdown render đúng và source được kiểm tra thủ công cho claim đã thay đổi.

## AI

AI-assisted contributions được welcome, nhưng AI không được dùng làm nguồn kỹ thuật.

Người submit phải đọc output và nói rõ phần chưa chắc nếu có.

## Review

Reviewer kiểm tra:

1. Concept có thực sự cần page riêng không?
2. Claim có đúng không?
3. Nguồn có support claim không?
4. Người mới có hiểu không?
5. Có thể viết ngắn hơn mà không đổi nghĩa không?

Xem [CONTENT_GUIDE.md](CONTENT_GUIDE.md).
