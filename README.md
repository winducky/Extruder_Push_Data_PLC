# Hệ Thống Điều Khiển Extruder

## Giới Thiệu
Phần mềm quản lý và điều khiển máy ép đùn (Extruder) trong sản xuất lốp xe. Hệ thống cho phép nhập kế hoạch sản xuất, quản lý thông số kỹ thuật và nạp dữ liệu xuống PLC.

## Tính Năng Chính

### 1. Quản Lý Kế Hoạch Sản Xuất
- **Nhập kế hoạch** (Import Plan): Đọc file Excel/CSV, tự động thêm các mã ExtCode vào danh sách sản xuất
- **Thay đổi thứ tự** (Change Plan): Kéo thả để sắp xếp thứ tự sản xuất theo mong muốn
- **Tự động load**: Mỗi khi khởi động, chương trình tự động load kế hoạch đầu tiên

### 2. Quản Lý Thông Số Kỹ Thuật
Hiển thị và quản lý các thông số cho từng mã sản phẩm:
- **Kích thước & Trọng lượng**: Chiều dài, chiều rộng, trọng lượng
- **Tốc độ**: Tốc độ trục vít trên/dưới, tốc độ con lăn, tốc độ TUC
- **Độ căng**: Độ căng băng tải, độ dốc, các thông số con lăn

### 3. Nạp Dữ Liệu PLC
- Chuyển thông số kỹ thuật xuống PLC
- Tự động xóa mã đã sản xuất khỏi danh sách kế hoạch
- Chuyển sang sản phẩm tiếp theo trong danh sách

### 4. Bảo Mật
- Xác thực Operator trước khi thực hiện các thao tác quan trọng
- Mật khẩu được ẩn khi nhập
- Ghi log đầy đủ lịch sử thao tác

## Công Nghệ Sử Dụng

- **Ngôn ngữ**: Python 3.x
- **GUI Framework**: PyQt5
- **Database**: SQLite3
- **Xử lý file**: pandas, openpyxl
- **Đóng gói**: PyInstaller

## Cấu Trúc Database

### Bảng `spec` - Thông số kỹ thuật
```sql
- ext_code (UNIQUE): Mã ép suất
- tire_name: Tên lốp
- length, height, weight: Kích thước, trọng lượng
- upper_screw_speed, lower_screw_speed: Tốc độ trục vít
- first_roller_speed, roll_tuc_speed: Tốc độ con lăn
- conveyor_roller, conveyor_slope: Độ căng băng tải
- roller_conveyor_belt, cooling_conveyor_belt: Thông số băng tải
- tuc_roller: Thông số TUC
