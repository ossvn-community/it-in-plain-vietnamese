# Content Guide

## Mục tiêu

Nội dung cần giải thích các khái niệm IT bằng tiếng Việt rõ ràng, dễ hiểu và chính xác cho người mới bắt đầu.

## Chọn concept

Không cần tạo một page riêng cho mọi thuật ngữ IT.

Ưu tiên concept:

- Giúp người mới hiểu hoặc sử dụng một mảng công nghệ cụ thể.
- Xuất hiện đủ thường xuyên để việc có một page riêng mang lại giá trị.
- Là nền tảng để hiểu nhiều concept khác hoặc có giá trị thực hành rõ ràng.
- Có phạm vi đủ rõ để giải thích trong một page.

Không thêm concept chỉ vì nó là kiến thức nền tảng về mặt học thuật. Nếu một ý quá hiển nhiên với đối tượng mục tiêu hoặc có thể giải thích đủ bằng một câu ngay trong concept khác, không nhất thiết phải có page riêng.

Các category nên đại diện cho một mảng công nghệ hoặc nhóm chủ đề rõ ràng, không dùng category chỉ để gom các kiến thức được xem là "cơ bản".

## Cấu trúc

Một concept không bắt buộc phải dùng cùng một bộ section với concept khác.

Sau phần mở đầu, chỉ thêm các section thực sự giúp người đọc hiểu concept. Một số section thường dùng:

- `Vai trò`
- `Tại sao cần nó?`
- `Đặc điểm`
- `Các loại phổ biến`
- `Nó hoạt động thế nào?`
- `Ví dụ`
- `So sánh`
- `Thử ngay`
- `Dễ nhầm với gì?`
- `Đọc tiếp`
- `Nguồn`

Không cần dùng tất cả và không bắt buộc theo thứ tự trên. Tên section cũng có thể thay đổi để phù hợp với nội dung.

Trong concept hoàn chỉnh, phần ngay sau tiêu đề nên trả lời trực tiếp câu hỏi của concept. Không cần thêm section `30 giây` hoặc `Khái quát` chỉ để chứa phần mở đầu.

`Khái quát` trong `_template.md` chỉ là hướng dẫn cho contributor khi bắt đầu viết.

## Metadata

Mỗi concept dùng front matter với các field:

```yaml
title: "Tên concept"
category: "software-development"
core: false
status: "draft"
last_reviewed: "YYYY-MM-DD"
reviewers: []
```

`category` phải thuộc một trong 9 mảng:

- `software-development`
- `git-open-source`
- `web`
- `systems-networking`
- `data`
- `security`
- `cloud-devops`
- `ai`
- `embedded-iot`

`core: true` nghĩa là concept thuộc nhóm **5 khái niệm nên đọc trước** của mảng. Không dùng `core: true` chỉ vì một concept được xem là quan trọng. Việc chọn hoặc thay đổi nhóm này phải xét nền tảng, mức độ thường gặp, giá trị thực hành, overlap và learning path.

Concept mới mặc định dùng `core: false` trừ khi PR đang thay đổi nhóm 5 khái niệm nên đọc trước và có lý do rõ ràng.

## Viết cho người mới

Giả định người đọc chưa có nền tảng kỹ thuật về concept đang đọc.

- Ưu tiên từ phổ thông và câu ngắn.
- Giải thích ý chính trước khi đi sâu vào chi tiết kỹ thuật.
- Thuật ngữ chuyên môn cần được giải thích khi xuất hiện lần đầu nếu người mới có thể chưa biết.
- Không dùng một khái niệm khó hơn để giải thích một khái niệm cơ bản mà không giải thích thêm.
- Giữ thuật ngữ tiếng Anh khi nó phổ biến trong ngành hoặc hữu ích cho việc tra cứu.
- Ưu tiên ví dụ quen thuộc hoặc tình huống thực tế khi chúng giúp người đọc hiểu nhanh hơn.
- Có thể đơn giản hóa cách giải thích, nhưng không được làm sai bản chất của concept.
- Phần mở đầu nên có thể hiểu được mà không yêu cầu người đọc phải đọc một concept khác trước.

## Cách viết

- Một page = một concept.
- Kết luận trước, giải thích sau.
- Ưu tiên câu và paragraph ngắn.
- Giải thích acronym ở lần xuất hiện đầu tiên.
- Nếu dùng analogy, nói rõ đó là so sánh đơn giản hóa.
- Không dùng AI làm nguồn.

## Nguồn

Mỗi concept phải có ít nhất một nguồn đáng tin cậy phù hợp với nội dung cần kiểm chứng.

Các loại nguồn phù hợp có thể gồm:

- Standard, specification hoặc RFC.
- Official documentation.
- Tài liệu từ trường đại học hoặc tổ chức giáo dục uy tín.
- Tài liệu kỹ thuật từ tổ chức hoặc dự án uy tín.
- Tài liệu tiếng Việt đáng tin cậy.
- Bài viết kỹ thuật có tác giả và cơ sở rõ ràng.

Dùng nguồn đáng tin cậy để đảm bảo độ chính xác, nhưng trình bày nội dung theo cách dễ hiểu cho người mới.

Không bắt buộc mọi câu trong bài phải có citation riêng. Mọi source trong concept phải là Markdown link trực tiếp tới tài liệu đã dùng.

Ví dụ:

```md
- [GitHub Docs - About Git](https://docs.github.com/en/get-started/using-git/about-git)
```

## Status

- `draft` - chưa qua review phù hợp.
- `reviewed` - đã qua content/technical review cần thiết.

Chỉ thêm trạng thái khác khi có nhu cầu thật.

## Review checklist

- Concept có thực sự cần một page riêng cho người mới không?
- Claim kỹ thuật đúng và có nguồn đáng tin cậy hỗ trợ.
- Phần mở đầu trả lời trực tiếp câu hỏi của concept.
- Người mới có thể hiểu ý chính mà không cần nền tảng sâu.
- Thuật ngữ chuyên môn được giải thích khi cần.
- Không có chi tiết kỹ thuật không cần thiết làm phần giải thích khó hiểu hơn.
- Ví dụ hoặc analogy không làm sai bản chất.
- Cấu trúc phù hợp với concept, không thêm section chỉ để theo template.
- Nội dung có thể viết đơn giản hơn mà vẫn chính xác hay không?
