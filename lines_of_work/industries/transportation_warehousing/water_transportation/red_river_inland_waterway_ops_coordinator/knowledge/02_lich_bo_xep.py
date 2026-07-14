title = "Lập lịch bốc xếp hàng hóa"

content = """
- Dựa trên danh sách tàu đang chờ, năng lực cầu cảng (số lượng cần cẩu, năng suất tấn/giờ), số lượng nhân công và thời gian làm việc (ca ngày/ca đêm), lập lịch bốc xếp ưu tiên.
- Sử dụng nguyên tắc FIFO (First In First Out) nhưng có ngoại lệ: tàu chở hàng nguy hiểm (loại 1,2,3 theo IMO) được ưu tiên trước; tàu chở hàng tươi sống, hàng cứu trợ được ưu tiên trong vòng 4 giờ kể từ khi đến.
- Mỗi cầu cảng chỉ bố trí tối đa 2 cần cẩu hoạt động đồng thời để tránh va chạm. Khoảng cách an toàn giữa các cần cẩu tối thiểu 5 mét.
- Thời gian bốc xếp trung bình: container 20ft: 3-5 phút; container 40ft: 5-8 phút; hàng rời (xi măng, phân bón): 50-80 tấn/giờ/cần cẩu. Điều chỉnh theo điều kiện thời tiết (mưa lớn giảm 30% năng suất).
- Lịch phải được phê duyệt bởi Trưởng ca trước 30 phút so với giờ bắt đầu ca. Gửi lịch đến đội bốc xếp, đại lý tàu và hải quan ít nhất 1 giờ trước khi thực hiện.
"""  # noqa: E501

version = "0.0.1"
