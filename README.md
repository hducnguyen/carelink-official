# CareLink - Hệ thống Quản lý Phòng khám | Clinic Management System

## Giới thiệu | Introduction

**Tiếng Việt:**  
CareLink là một dự án cộng đồng mã nguồn mở được phát triển nhằm hỗ trợ chuyển đổi số cho các phòng khám tư nhân và các bác sĩ hành nghề độc lập. Dự án được xây dựng trên nền tảng Django (Python) - một framework mạnh mẽ, linh hoạt và dễ tùy chỉnh.

**English:**  
CareLink is an open-source community project developed to support digital transformation for private clinics and independent practitioners. The project is built on the Django (Python) framework - a powerful, flexible, and easily customizable platform.

## Mục đích của dự án | Project Purpose

**Tiếng Việt:**  
Dự án CareLink ra đời với mục tiêu:

- **Góp phần vào quá trình chuyển đổi số** trong lĩnh vực y tế, đặc biệt là các phòng khám tư nhân
- **Giảm tải công việc giấy tờ** cho các bác sĩ, giúp họ tập trung nhiều hơn vào việc chăm sóc bệnh nhân
- **Tối ưu hóa quy trình làm việc** của phòng khám, từ đặt lịch khám đến quản lý hồ sơ bệnh nhân
- **Giảm chi phí vận hành**, từ đó có thể giảm chi phí khám chữa bệnh, giúp nhiều người dân có cơ hội tiếp cận dịch vụ y tế chất lượng với giá cả phải chăng

**English:**  
The CareLink project was created with the following goals:

- **Contributing to digital transformation** in healthcare, especially for private clinics
- **Reducing paperwork** for doctors, allowing them to focus more on patient care
- **Optimizing clinic workflows**, from appointment scheduling to patient record management
- **Reducing operational costs**, thereby lowering healthcare expenses, making quality healthcare services more accessible to ordinary people

## Tính năng chính | Key Features

**Tiếng Việt:**
- **Quản lý lịch hẹn**: Đặt lịch trực tuyến, nhắc nhở tự động
- **Hồ sơ bệnh nhân**: Lưu trữ thông tin bệnh nhân, lịch sử khám chữa bệnh
- **Quản lý nhân viên**: Phân quyền, quản lý lịch làm việc
- **Báo cáo thống kê**: Theo dõi hoạt động phòng khám
- **Hỗ trợ đa ngôn ngữ**: Tiếng Việt và tiếng Anh
- **Giao diện thân thiện**: Dễ sử dụng trên nhiều thiết bị

**English:**
- **Appointment Management**: Online booking, automatic reminders
- **Patient Records**: Store patient information, medical history
- **Staff Management**: Role-based access control, work schedule management
- **Reports and Statistics**: Monitor clinic activities
- **Multilingual Support**: Vietnamese and English
- **User-friendly Interface**: Easy to use across various devices

## Ưu điểm kỹ thuật | Technical Advantages

### Xây dựng trên Django (Python) | Built on Django (Python)

**Tiếng Việt:**  
CareLink được phát triển bằng Django - một framework Python mạnh mẽ với nhiều ưu điểm:

- **Dễ học và sử dụng**: Python là ngôn ngữ dễ tiếp cận, phù hợp với cả người mới bắt đầu
- **Phát triển nhanh**: Django cung cấp nhiều công cụ và thư viện giúp phát triển ứng dụng nhanh chóng
- **Bảo mật cao**: Django có sẵn nhiều tính năng bảo mật như chống SQL injection, CSRF, XSS
- **Khả năng mở rộng**: Dễ dàng thêm tính năng mới khi nhu cầu tăng lên

**English:**  
CareLink is developed using Django - a powerful Python framework with many advantages:

- **Easy to learn and use**: Python is an accessible language, suitable for beginners
- **Rapid development**: Django provides many tools and libraries for quick application development
- **High security**: Django has built-in security features like protection against SQL injection, CSRF, XSS
- **Scalability**: Easily add new features as needs grow

### Dễ dàng tùy chỉnh | Easy Customization

**Tiếng Việt:**
- **Kiến trúc module**: Được chia thành các ứng dụng con (app_booking, app_patient, app_staff...) giúp dễ dàng tùy chỉnh theo nhu cầu
- **Giao diện linh hoạt**: Sử dụng Bootstrap 5 và crispy forms cho phép tùy biến giao diện dễ dàng
- **Cấu hình đơn giản**: Tập trung vào file settings.py để điều chỉnh các thông số hệ thống

**English:**
- **Modular architecture**: Divided into sub-applications (app_booking, app_patient, app_staff...) making it easy to customize according to needs
- **Flexible interface**: Using Bootstrap 5 and crispy forms allows for easy interface customization
- **Simple configuration**: Focus on settings.py file to adjust system parameters

## Hướng dẫn cài đặt | Installation Guide

### Yêu cầu hệ thống | System Requirements
**Tiếng Việt:**
- Python 3.8+
- MySQL
- Các thư viện phụ thuộc (xem requirements.txt)

**English:**
- Python 3.8+
- MySQL
- Dependencies (see requirements.txt)

### Các bước cài đặt | Installation Steps

**Tiếng Việt:**

1. Clone repository về máy:
```bash
git clone https://github.com/hducnguyen/carelink-official.git
cd carelink
```

2. Tạo và kích hoạt môi trường ảo:
```bash
python -m venv venv
source venv/bin/activate  # Trên Linux/Mac
venv\Scripts\activate  # Trên Windows
```

3. Cài đặt các gói phụ thuộc:
```bash
pip install -r requirements.txt
```

4. Cấu hình cơ sở dữ liệu trong settings.py

5. Chạy migration:
```bash
python manage.py migrate
```

6. Tạo tài khoản admin:
```bash
python manage.py createsuperuser
```

7. Khởi động server:
```bash
python manage.py runserver
```

**English:**

1. Clone the repository:
```bash
git clone https://github.com/hducnguyen/carelink-official.git
cd carelink
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Linux/Mac
venv\Scripts\activate  # On Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure the database in settings.py

5. Run migrations:
```bash
python manage.py migrate
```

6. Create admin account:
```bash
python manage.py createsuperuser
```

7. Start the server:
```bash
python manage.py runserver
```

## Đóng góp cho dự án | Contributing to the Project

**Tiếng Việt:**  
Chúng tôi rất hoan nghênh mọi đóng góp từ cộng đồng. Bạn có thể tham gia bằng cách:

- Báo cáo lỗi hoặc đề xuất tính năng mới
- Đóng góp mã nguồn thông qua Pull Request
- Cải thiện tài liệu
- Chia sẻ dự án đến những người có thể được hưởng lợi

**English:**  
We welcome all contributions from the community. You can participate by:

- Reporting bugs or suggesting new features
- Contributing code through Pull Requests
- Improving documentation
- Sharing the project with potential beneficiaries

## Giấy phép | License

**Tiếng Việt:**  
Dự án được phát hành dưới giấy phép MIT. Xem file LICENSE để biết thêm chi tiết.

**English:**  
The project is released under the MIT license. See the LICENSE file for more details.

## Liên hệ | Contact

**Tiếng Việt:**  
Nếu bạn có câu hỏi hoặc đề xuất, vui lòng liên hệ qua:
- Email: jackyboy.vinshool@gmail.com
- GitHub Issues: [https://github.com/hducnguyen/carelink-official/issues](https://github.com/hducnguyen/carelink-official/issues)

**English:**  
If you have questions or suggestions, please contact us via:
- Email: jackyboy.vinshool@gmail.com
- GitHub Issues: [https://github.com/hducnguyen/carelink-official/issues](https://github.com/hducnguyen/carelink-official/issues)

---

*CareLink - Chăm sóc sức khỏe vì cộng đồng | Healthcare for the community*
