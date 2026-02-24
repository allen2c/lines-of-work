title = "Patterns phân trang"

content = """
Pagination cho phép client lấy large dataset từng phần. Offset-based và cursor-based
là hai approach chính. Chọn đúng pattern ảnh hưởng consistency và performance.

**Offset-based:** page=2, limit=20. Đơn giản. Nhưng inconsistent khi data thay đổi
giữa requests — item có thể skip hoặc duplicate. OK cho static data. Bad cho
real-time. OFFSET chậm khi offset lớn (DB scan).

**Cursor-based:** cursor=abc123, limit=20. Cursor từ item cuối page trước. Consistent
— dựa trên position. Better performance — index seek. Không jump to page N. Standard
cho feed, stream. Include next_cursor trong response.

**Keyset Pagination:** Cursor là (id, created_at) của last item. WHERE id > ?
ORDER BY id LIMIT. Efficient. Consistent. Không expose internal cursor. Page size
configurable, với max limit.
"""  # noqa: E501

version = "0.0.1"
