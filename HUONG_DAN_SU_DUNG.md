# Hướng Dẫn Sử Dụng Phần Mềm Quản Lý Instance MuMu

## Giới Thiệu

Phần mềm Quản Lý Instance MuMu là một ứng dụng Python được thiết kế để quản lý các instance của MuMu Emulator 12 một cách dễ dàng và hiệu quả. Phần mềm cung cấp cả giao diện dòng lệnh (CLI) và giao diện đồ họa (GUI) để thao tác với các emulator.

## Tính Năng Chính

- **Quản lý Instance**: Tạo, sao chép, xóa, đổi tên emulator
- **Điều khiển Emulator**: Khởi động, tắt, khởi động lại emulator
- **Quản lý Ứng dụng**: Cài đặt APK, quản lý ứng dụng
- **Sao lưu và Phục hồi**: Backup emulator với tùy chọn nén
- **Giao diện Thân thiện**: Cả CLI và GUI để phù hợp với mọi người dùng
- **Tự động hóa**: Scripts mẫu cho các tác vụ thường gặp

## Cài Đặt và Cấu Hình

### Yêu Cầu Hệ Thống

- Python 3.7 trở lên
- MuMu Emulator 12 (phiên bản V4.0.0.3179 trở lên)
- Windows Operating System

### Cài Đặt

1. **Tải về các file của phần mềm**:
   - `instance_manager.py` - Module chính
   - `gui_manager.py` - Giao diện đồ họa
   - `examples.py` - Các ví dụ sử dụng
   - `config.json` - File cấu hình

2. **Cấu hình đường dẫn MuMuManager.exe**:
   Chỉnh sửa file `config.json` để thiết lập đường dẫn đến `MuMuManager.exe`:
   ```json
   {
     "mumu_manager_path": "C:\\Program Files\\Netease\\MuMuPlayer-12.0\\shell\\MuMuManager.exe"
   }
   ```

3. **Kiểm tra cài đặt**:
   ```bash
   python instance_manager.py info
   ```

## Hướng Dẫn Sử Dụng

### 1. Sử Dụng Giao Diện Dòng Lệnh (CLI)

#### Cú pháp cơ bản:
```bash
python instance_manager.py <command> [arguments]
```

#### Các lệnh thường dùng:

**Xem thông tin emulator:**
```bash
# Xem tất cả emulator
python instance_manager.py info

# Xem emulator cụ thể
python instance_manager.py info 0
```

**Tạo emulator mới:**
```bash
# Tạo 1 emulator
python instance_manager.py create

# Tạo 5 emulator
python instance_manager.py create 3 5
```

**Sao chép emulator:**
```bash
# Sao chép emulator index 0
python instance_manager.py clone 0

# Sao chép emulator index 0, tạo 3 bản copy
python instance_manager.py clone 0 3
```

**Khởi động/Tắt emulator:**
```bash
# Khởi động emulator
python instance_manager.py launch 0

# Tắt emulator
python instance_manager.py shutdown 0

# Khởi động lại emulator
python instance_manager.py restart 0
```

**Cài đặt ứng dụng:**
```bash
# Cài đặt APK vào emulator
python instance_manager.py install 0 "C:\\path\\to\\app.apk"
```

**Sao lưu emulator:**
```bash
# Backup emulator
python instance_manager.py backup 0 "C:\\backups" "my_backup"
```

### 2. Sử Dụng Giao Diện Đồ Họa (GUI)

**Khởi động GUI:**
```bash
python gui_manager.py
```

**Các chức năng GUI:**

1. **Danh sách Emulator**: Hiển thị tất cả emulator với thông tin trạng thái
2. **Nút điều khiển**:
   - **Refresh**: Cập nhật danh sách emulator
   - **Create**: Tạo emulator mới
   - **Clone**: Sao chép emulator đã chọn
   - **Delete**: Xóa emulator đã chọn
   - **Rename**: Đổi tên emulator
   - **Launch**: Khởi động emulator
   - **Shutdown**: Tắt emulator
   - **Restart**: Khởi động lại emulator
   - **Install APK**: Cài đặt ứng dụng
   - **Backup**: Sao lưu emulator

3. **Thanh trạng thái**: Hiển thị thông tin về tiến trình đang thực hiện

### 3. Sử Dụng Scripts Mẫu

**Chạy các ví dụ:**
```bash
python examples.py
```

**Các ví dụ có sẵn:**
- Thao tác cơ bản với emulator
- Thao tác hàng loạt
- Cài đặt ứng dụng tự động
- Backup tự động
- Thiết lập farm emulator
- Script giám sát emulator
- Quản lý cấu hình

## Tính Năng Nâng Cao

### 1. Quản Lý Hàng Loạt

**Thao tác với nhiều emulator:**
```python
from instance_manager import MuMuInstanceManager

manager = MuMuInstanceManager()

# Khởi động tất cả emulator
manager.launch_emulator("all")

# Khởi động emulator cụ thể
manager.launch_emulator([0, 1, 2])
```

### 2. Tự Động Hóa

**Tạo script tự động:**
```python
# Tạo farm 10 emulator
def setup_farm():
    manager = MuMuInstanceManager()
    
    # Tạo 10 emulator
    manager.create_emulator(count=10)
    
    # Đặt tên cho từng emulator
    emulators = manager.get_emulator_info("all")
    for i, emu in enumerate(emulators[-10:]):
        manager.rename_emulator(emu.index, f"Farm_{i+1:02d}")
    
    # Khởi động tất cả
    manager.launch_emulator("all")
```

### 3. Giám Sát và Bảo Trì

**Script giám sát tự động:**
```python
def monitor_and_restart():
    manager = MuMuInstanceManager()
    
    while True:
        emulators = manager.get_emulator_info("all")
        for emu in emulators:
            if not emu.is_process_started:
                print(f"Restarting emulator {emu.index}")
                manager.launch_emulator(emu.index)
        
        time.sleep(60)  # Kiểm tra mỗi phút
```

## Cấu Hình Chi Tiết

### File config.json

```json
{
  "mumu_manager_path": "MuMuManager.exe",
  "default_backup_dir": "./backups",
  "auto_refresh_interval": 5,
  "max_concurrent_operations": 3,
  "timeout_settings": {
    "command_timeout": 60,
    "startup_timeout": 120,
    "shutdown_timeout": 60
  },
  "logging": {
    "enabled": true,
    "log_file": "instance_manager.log",
    "log_level": "INFO"
  },
  "ui_settings": {
    "window_width": 800,
    "window_height": 600,
    "theme": "default"
  }
}
```

### Các tham số quan trọng:

- `mumu_manager_path`: Đường dẫn đến MuMuManager.exe
- `default_backup_dir`: Thư mục backup mặc định
- `timeout_settings`: Thời gian chờ cho các thao tác
- `max_concurrent_operations`: Số thao tác tối đa cùng lúc

## Xử Lý Lỗi và Khắc Phục

### Lỗi thường gặp:

1. **"MuMuManager.exe not found"**
   - Kiểm tra đường dẫn trong config.json
   - Đảm bảo MuMu Emulator đã được cài đặt

2. **"Failed to get emulator info"**
   - Kiểm tra quyền truy cập
   - Đảm bảo MuMu Emulator đang chạy

3. **"Command timed out"**
   - Tăng timeout trong config.json
   - Kiểm tra tài nguyên hệ thống

### Debug và Logging:

Bật logging trong config.json để theo dõi các lỗi:
```json
{
  "logging": {
    "enabled": true,
    "log_file": "instance_manager.log",
    "log_level": "DEBUG"
  }
}
```

## Tích Hợp và Mở Rộng

### Tích hợp vào hệ thống khác:

```python
# Import module
from instance_manager import MuMuInstanceManager

# Sử dụng trong ứng dụng của bạn
def my_automation_task():
    manager = MuMuInstanceManager()
    
    # Thực hiện các thao tác tự động
    emulators = manager.get_emulator_info("all")
    for emu in emulators:
        if emu.player_state == "stopped":
            manager.launch_emulator(emu.index)
```

### Mở rộng chức năng:

Phần mềm được thiết kế để dễ dàng mở rộng. Bạn có thể:
- Thêm các phương thức mới vào class `MuMuInstanceManager`
- Tạo GUI tùy chỉnh
- Thêm các script automation riêng

## Hỗ Trợ và Cộng Đồng

### Báo cáo lỗi:
- Tạo issue trên GitHub repository
- Cung cấp log file và mô tả chi tiết

### Đóng góp:
- Fork repository và tạo pull request
- Tuân thủ coding standards
- Thêm tests cho các tính năng mới

## Changelog và Cập Nhật

### Version 1.0.0
- Phiên bản đầu tiên
- Hỗ trợ tất cả tính năng cơ bản của MuMuManager
- Giao diện CLI và GUI
- Scripts mẫu và documentation

### Kế hoạch tương lai:
- Thêm web interface
- Hỗ trợ remote management
- Tích hợp với cloud services
- Mobile app companion

## Liên Hệ

- Repository: [GitHub Link]
- Email: [Support Email]
- Documentation: [Documentation Link]

---

**Lưu ý**: Đây là phần mềm wrapper cho MuMuManager.exe. Đảm bảo bạn có bản quyền sử dụng MuMu Emulator và tuân thủ các điều khoản sử dụng của NetEase.